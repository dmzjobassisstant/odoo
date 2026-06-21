from odoo import models, fields, api


class HrIssueNote(models.Model):
    _name = 'hr.issue.note'
    _description = 'HR Issue Internal Note'
    _order = 'date desc'

    issue_id = fields.Many2one(
        'hr.issue',
        string='Issue',
        required=True,
        ondelete='cascade',
    )
    author_id = fields.Many2one(
        'hr.employee',
        string='Author',
        default=lambda self: self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)], limit=1
        ),
        readonly=True,
    )
    note = fields.Text(
        string='Note',
        required=True,
    )
    date = fields.Datetime(
        string='Date',
        default=fields.Datetime.now,
        readonly=True,
    )
    is_visible_to_employee = fields.Boolean(
        string='Visible to Employee',
        default=False,
        help='If checked, the reporting employee can see this note.',
    )
