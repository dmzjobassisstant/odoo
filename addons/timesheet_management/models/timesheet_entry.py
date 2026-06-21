from odoo import models, fields, api, _
from odoo.exceptions import UserError


class TimesheetEntry(models.Model):
    _name = 'timesheet.entry'
    _description = 'Timesheet Entry'
    _order = 'date, task_id, id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    week_id = fields.Many2one(
        'timesheet.week',
        string='Timesheet Week',
        required=True,
        ondelete='cascade',
        tracking=True,
    )
    date = fields.Date(
        string='Date',
        required=True,
        tracking=True,
    )
    day_name = fields.Char(
        string='Day',
        compute='_compute_day_name',
        store=True,
        readonly=True,
    )
    task_id = fields.Many2one(
        'project.task',
        string='Task',
        required=True,
        tracking=True,
        domain="[('user_ids', 'in', [week_id.employee_id.id]), "
               " '|', ('user_ids', '=', False)]",
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        related='task_id.project_id',
        store=True,
    )
    description = fields.Text(
        string='Description',
        tracking=True,
    )
    hours = fields.Float(
        string='Hours',
        default=0.0,
        tracking=True,
    )

    # ---- Computed ----

    @api.depends('date')
    def _compute_day_name(self):
        """Compute the short day name from the date."""
        DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for rec in self:
            if rec.date:
                rec.day_name = DAY_NAMES[rec.date.weekday()]
            else:
                rec.day_name = ''

    # ---- Onchange helpers ----

    @api.onchange('week_id')
    def _onchange_week_id(self):
        """Reset task_id when the week changes so domain re-evaluates."""
        if self.week_id:
            self.task_id = False

    # ---- Write guard ----

    def write(self, vals):
        """Prevent editing entries on timesheets that are not in draft."""
        for rec in self:
            if rec.week_id.state != 'draft':
                is_admin = self.env.user.has_group(
                    'timesheet_management.group_timesheet_admin'
                )
                if not is_admin:
                    raise UserError(_(
                        'Timesheet "%s" is in %s state. You cannot modify entries. '
                        'Contact an administrator to unlock it first.'
                    ) % (rec.week_id.name, dict(rec.week_id._fields['state'].selection).get(
                        rec.week_id.state, rec.week_id.state)))
        return super().write(vals)

    def unlink(self):
        """Prevent deleting entries on timesheets that are not in draft."""
        for rec in self:
            if rec.week_id.state != 'draft':
                is_admin = self.env.user.has_group(
                    'timesheet_management.group_timesheet_admin'
                )
                if not is_admin:
                    raise UserError(_(
                        'Timesheet "%s" is in %s state. You cannot delete entries. '
                        'Contact an administrator to unlock it first.'
                    ) % (rec.week_id.name, dict(rec.week_id._fields['state'].selection).get(
                        rec.week_id.state, rec.week_id.state)))
        return super().unlink()
