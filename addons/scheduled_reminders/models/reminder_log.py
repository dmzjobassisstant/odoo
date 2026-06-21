from odoo import models, fields


class ReminderLog(models.Model):
    _name = 'reminder.log'
    _description = 'Reminder Log'
    _order = 'sent_date desc'
    _rec_name = 'rule_id'

    rule_id = fields.Many2one(
        'reminder.rule',
        string='Reminder Rule',
        required=True,
        readonly=True,
        ondelete='cascade',
    )
    record_id = fields.Integer(
        string='Record ID',
        required=True,
        readonly=True,
    )
    record_model = fields.Char(
        string='Record Model',
        required=True,
        readonly=True,
    )
    sent_date = fields.Datetime(
        string='Sent Date',
        required=True,
        readonly=True,
        default=fields.Datetime.now,
    )
    recipient_id = fields.Many2one(
        'res.users',
        string='Recipient',
        required=True,
        readonly=True,
    )
    message = fields.Text(
        string='Message',
        readonly=True,
    )
    acknowledged = fields.Boolean(
        string='Acknowledged',
        default=False,
    )

    def action_acknowledge(self):
        """Mark this reminder as acknowledged."""
        self.write({'acknowledged': True})
        return True
