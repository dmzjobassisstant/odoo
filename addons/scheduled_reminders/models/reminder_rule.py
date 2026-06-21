import json
import logging
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ReminderRule(models.Model):
    _name = 'reminder.rule'
    _description = 'Reminder Rule'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    model = fields.Selection([
        ('timesheet.week', 'Timesheet Week'),
        ('hr.payslip', 'Payslip'),
        ('training.assignment', 'Training Assignment'),
        ('hr.offboarding', 'Employee Offboarding'),
    ], string='Model', required=True)
    trigger_type = fields.Selection([
        ('state', 'Check Record State'),
        ('date', 'Check Date Field'),
    ], string='Trigger Type', required=True, default='state')
    trigger_domain = fields.Text(
        string='Trigger Domain',
        help='Odoo domain as a JSON string, e.g. [["state","=","draft"]]',
        default='[]',
    )
    trigger_date_field = fields.Char(
        string='Trigger Date Field',
        help='Technical name of the date field to check (for date triggers)',
    )
    remind_before_days = fields.Integer(
        string='Remind Before (Days)',
        default=0,
        help='Send reminder N days before the trigger date. 0 = on the date itself.',
    )
    message_template = fields.Text(
        string='Message Template',
        help='Body of the notification. Use {{object.field_name}} for record values.',
    )
    recipient_field = fields.Char(
        string='Recipient Field',
        help='Path to the user on the record, e.g. "employee_id.user_id" or "create_uid"',
    )
    recipient_group_id = fields.Many2one(
        'res.groups',
        string='Recipient Group',
        help='Alternative to recipient_field: send to all users in this group.',
    )
    is_active = fields.Boolean(string='Active', default=True)
    last_checked = fields.Datetime(string='Last Checked', readonly=True)

    @api.constrains('trigger_type', 'trigger_date_field', 'trigger_domain')
    def _check_trigger_config(self):
        for rule in self:
            if rule.trigger_type == 'date' and not rule.trigger_date_field:
                raise UserError(_(
                    'Date trigger type requires a Trigger Date Field to be set.'
                ))
            if rule.trigger_type == 'state' and not rule.trigger_domain:
                raise UserError(_(
                    'State trigger type requires a Trigger Domain to be set.'
                ))

    @api.constrains('recipient_field', 'recipient_group_id')
    def _check_recipient(self):
        for rule in self:
            if not rule.recipient_field and not rule.recipient_group_id:
                raise UserError(_(
                    'You must set either a Recipient Field or a Recipient Group.'
                ))

    # ------------------------------------------------------------------
    # Cron entry point
    # ------------------------------------------------------------------

    @api.model
    def _evaluate_all(self):
        """Called by the cron job every 5 minutes. Evaluate all active rules."""
        _logger.info('Scheduled Reminders: starting evaluation of all active rules')
        rules = self.search([('is_active', '=', True)])
        total_logs = 0
        for rule in rules:
            try:
                count = rule._evaluate()
                total_logs += count
            except Exception as e:
                _logger.exception(
                    'Error evaluating reminder rule %s (id=%s): %s',
                    rule.name, rule.id, str(e)
                )
        _logger.info(
            'Scheduled Reminders: evaluation complete, %d reminders sent',
            total_logs
        )
        return True

    def _evaluate(self):
        """Evaluate a single rule and send reminders for matching records."""
        self.ensure_one()
        _logger.info('Evaluating rule: %s (model=%s, trigger=%s)',
                     self.name, self.model, self.trigger_type)

        # Build the search domain
        domain = self._build_search_domain()
        if domain is None:
            _logger.warning('Rule %s: could not build domain, skipping', self.name)
            return 0

        # Search for matching records
        Model = self.env[self.model]
        records = Model.search(domain)
        _logger.info('Rule %s: found %d matching records', self.name, len(records))

        # Process each record
        sent_count = 0
        for record in records:
            if self._send_reminder(record):
                sent_count += 1

        # Update last_checked
        self.write({'last_checked': fields.Datetime.now()})
        return sent_count

    def _build_search_domain(self):
        """Build the Odoo domain for searching matching records."""
        self.ensure_one()

        if self.trigger_type == 'state':
            # Parse trigger_domain JSON
            try:
                domain = json.loads(self.trigger_domain) if self.trigger_domain else []
            except json.JSONDecodeError:
                _logger.error(
                    'Rule %s: invalid trigger_domain JSON: %s',
                    self.name, self.trigger_domain
                )
                return None
            return domain

        elif self.trigger_type == 'date':
            if not self.trigger_date_field:
                return None

            # Calculate the target date: today + remind_before_days
            today = fields.Date.today()
            target_date = today + timedelta(days=self.remind_before_days)

            # Build domain: records where trigger_date_field = target_date
            domain = [(self.trigger_date_field, '=', target_date)]

            # Add extra domain conditions if specified
            if self.trigger_domain:
                try:
                    extra = json.loads(self.trigger_domain)
                    domain.extend(extra)
                except json.JSONDecodeError:
                    _logger.error(
                        'Rule %s: invalid trigger_domain JSON in date trigger',
                        self.name
                    )

            return domain

        return None

    def _resolve_recipient(self, record):
        """Resolve the recipient user(s) for a given record.

        Returns a recordset of res.users (may be empty).
        """
        self.ensure_one()

        # Option 1: recipient_field (path to user on the record)
        if self.recipient_field:
            try:
                # Walk the dotted path
                obj = record
                for part in self.recipient_field.split('.'):
                    obj = obj[part]
                if obj and obj._name == 'res.users':
                    return obj
            except Exception:
                _logger.debug(
                    'Rule %s: could not resolve recipient_field "%s" on record %s (id=%s)',
                    self.name, self.recipient_field, record._name, record.id
                )

        # Option 2: recipient_group (all users in group)
        if self.recipient_group_id:
            return self.recipient_group_id.users

        return self.env['res.users']

    def _send_reminder(self, record):
        """Send a reminder for a single record. Returns True if sent."""
        self.ensure_one()

        # Check for duplicate (already logged for this rule + record)
        existing_log = self.env['reminder.log'].search([
            ('rule_id', '=', self.id),
            ('record_id', '=', record.id),
            ('record_model', '=', record._name),
        ], limit=1)

        if existing_log:
            _logger.debug(
                'Rule %s: already sent for record %s (id=%s), skipping',
                self.name, record._name, record.id
            )
            return False

        # Resolve recipient
        recipients = self._resolve_recipient(record)
        if not recipients:
            _logger.debug(
                'Rule %s: no recipient found for record %s (id=%s), skipping',
                self.name, record._name, record.id
            )
            return False

        # Render message template
        message = self._render_message(record)

        # Create mail.activity for each recipient
        activity_type = self.env.ref(
            'mail.mail_activity_data_todo', raise_if_not_found=False
        )
        if not activity_type:
            _logger.warning(
                'Rule %s: mail.mail_activity_data_todo not found, skipping',
                self.name
            )
            return False

        for user in recipients:
            # Create activity on the record for this user
            self.env['mail.activity'].create({
                'activity_type_id': activity_type.id,
                'res_id': record.id,
                'res_model_id': self.env['ir.model']._get(record._name).id,
                'res_model': record._name,
                'user_id': user.id,
                'summary': self.name,
                'note': message,
                'date_deadline': fields.Date.today(),
            })

            # Log the reminder
            self.env['reminder.log'].create({
                'rule_id': self.id,
                'record_id': record.id,
                'record_model': record._name,
                'sent_date': fields.Datetime.now(),
                'recipient_id': user.id,
                'message': message,
            })

            _logger.info(
                'Rule %s: sent reminder to %s for record %s (id=%s)',
                self.name, user.name, record._name, record.id
            )

        return True

    def _render_message(self, record):
        """Render the message template with record values.

        Supports {{object.field_name}} syntax.
        """
        self.ensure_one()
        template = self.message_template or ''
        if not template:
            return ''

        # Simple template rendering: replace {{object.field}} with actual values
        import re
        def replace_match(match):
            field_path = match.group(1).strip()
            try:
                obj = record
                for part in field_path.split('.'):
                    obj = obj[part]
                return str(obj) if obj else ''
            except Exception:
                return '{{%s}}' % field_path

        return re.sub(r'\{\{object\.([^}]+)\}\}', replace_match, template)

    # ------------------------------------------------------------------
    # Action: manually trigger evaluation
    # ------------------------------------------------------------------

    def action_evaluate_now(self):
        """Manually trigger evaluation of selected rules."""
        for rule in self:
            rule._evaluate()
        return True
