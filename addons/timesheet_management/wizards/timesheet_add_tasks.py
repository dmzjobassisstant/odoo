from odoo import models, fields, api, _


class TimesheetAddTasksWizard(models.TransientModel):
    _name = 'timesheet.add.tasks.wizard'
    _description = 'Add Tasks to Timesheet Week'

    week_id = fields.Many2one(
        'timesheet.week',
        string='Timesheet Week',
        required=True,
        readonly=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        related='week_id.employee_id',
        readonly=True,
    )
    task_ids = fields.Many2many(
        'project.task',
        string='Select Tasks',
        required=True,
        help='Selected tasks will be added to the timesheet with 7 day slots each.',
    )

    # ---- Domain for available tasks ----

    @api.onchange('week_id')
    def _onchange_week_id(self):
        """Filter tasks to employee's assigned tasks, excluding those already on the week."""
        if not self.week_id or not self.employee_id:
            self.task_ids = False
            return

        # Tasks already on this timesheet
        already_added = self.week_id.entry_ids.mapped('task_id').ids

        domain = [
            '|',
            ('user_ids', 'in', [self.employee_id.id]),
            ('user_ids', '=', False),
            ('project_id.active', '=', True),
            ('active', '=', True),
        ]
        if already_added:
            domain.append(('id', 'not in', already_added))

        return {'domain': {'task_ids': domain}}

    def action_add(self):
        """Create 7 day slots for each selected task."""
        self.ensure_one()
        if not self.task_ids:
            raise UserError(_('Please select at least one task.'))
        if self.week_id.state != 'draft':
            raise UserError(_('Timesheet is not in Draft state.'))

        created = self.week_id._add_tasks(self.task_ids.ids)
        self.week_id.message_post(body=_(
            '%(count)s task(s) added by %(user)s: %(tasks)s'
        ) % {
            'count': len(self.task_ids),
            'user': self.env.user.name,
            'tasks': ', '.join(self.task_ids.mapped('name')),
        })
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'timesheet.week',
            'res_id': self.week_id.id,
            'target': 'current',
        }
