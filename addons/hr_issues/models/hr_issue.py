from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HrIssue(models.Model):
    _name = 'hr.issue'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'HR Issue'
    _order = 'id desc'

    name = fields.Char(
        string='Reference',
        readonly=True,
        copy=False,
        default='New',
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        tracking=True,
    )
    reported_by = fields.Many2one(
        'hr.employee',
        string='Reported By',
        tracking=True,
        help='Person who reported this issue (if different from the employee)',
    )
    issue_type = fields.Selection(
        [
            ('grievance', 'Grievance'),
            ('dispute', 'Dispute'),
            ('harassment', 'Harassment'),
            ('discrimination', 'Discrimination'),
            ('conduct', 'Conduct'),
            ('attendance', 'Attendance'),
            ('other', 'Other'),
        ],
        string='Issue Type',
        required=True,
        tracking=True,
    )
    severity = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        string='Severity',
        default='medium',
        required=True,
        tracking=True,
    )
    description = fields.Text(
        string='Description',
        tracking=True,
    )
    resolution = fields.Text(
        string='Resolution',
        tracking=True,
    )
    resolution_date = fields.Date(
        string='Resolution Date',
        tracking=True,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('investigating', 'Investigating'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed'),
        ],
        string='State',
        default='draft',
        required=True,
        tracking=True,
    )
    assigned_to = fields.Many2one(
        'hr.employee',
        string='Assigned To',
        tracking=True,
    )
    is_confidential = fields.Boolean(
        string='Confidential',
        default=False,
        tracking=True,
        help='If marked confidential, only the reporter, assigned person, '
             'and HR manager can view this issue.',
    )
    date_reported = fields.Date(
        string='Date Reported',
        default=fields.Date.today,
        tracking=True,
    )
    target_resolution_date = fields.Date(
        string='Target Resolution Date',
        tracking=True,
    )
    note_ids = fields.One2many(
        'hr.issue.note',
        'issue_id',
        string='Internal Notes',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'hr.issue') or 'New'
        return super().create(vals_list)

    def _check_state_change_allowed(self):
        """Check if the current user can change the state of this issue."""
        self.ensure_one()
        user = self.env.user
        if user.has_group('hr_issues.group_hr_issue_manager'):
            return True
        employee = self.env['hr.employee'].search(
            [('user_id', '=', user.id)], limit=1)
        if self.assigned_to and self.assigned_to == employee:
            return True
        raise UserError(_(
            'Only the assigned person or an HR Manager can change '
            'the state of this issue.'))

    def action_open(self):
        for record in self:
            record._check_state_change_allowed()
            if record.state != 'draft':
                raise UserError(_('Only draft issues can be opened.'))
            record.write({
                'state': 'open',
                'date_reported': record.date_reported or fields.Date.today(),
            })
        return True

    def action_investigate(self):
        for record in self:
            record._check_state_change_allowed()
            if record.state != 'open':
                raise UserError(_(
                    'Only open issues can be moved to investigation.'))
            record.state = 'investigating'
        return True

    def action_resolve(self):
        for record in self:
            record._check_state_change_allowed()
            if record.state not in ('open', 'investigating'):
                raise UserError(_(
                    'Only open or investigating issues can be resolved.'))
            record.write({
                'state': 'resolved',
                'resolution_date': fields.Date.today(),
            })
        return True

    def action_close(self):
        for record in self:
            record._check_state_change_allowed()
            if record.state != 'resolved':
                raise UserError(_('Only resolved issues can be closed.'))
            record.state = 'closed'
        return True

    def action_reopen(self):
        for record in self:
            record._check_state_change_allowed()
            if record.state not in ('resolved', 'closed'):
                raise UserError(_(
                    'Only resolved or closed issues can be reopened.'))
            record.state = 'open'
        return True

    def action_set_draft(self):
        for record in self:
            record._check_state_change_allowed()
            record.state = 'draft'
        return True
