from odoo import fields, models


class HROffboardingTask(models.Model):
    _name = 'hr.offboarding.task'
    _description = 'Offboarding Task'
    _order = 'name'

    name = fields.Char(
        string='Task Name',
        required=True,
    )
    offboarding_id = fields.Many2one(
        'hr.offboarding',
        string='Offboarding',
        ondelete='cascade',
    )
    assigned_to = fields.Many2one(
        'hr.employee',
        string='Assigned To',
    )
    completed = fields.Boolean(
        string='Completed',
        default=False,
    )
    completed_date = fields.Date(
        string='Completed Date',
    )
    notes = fields.Text(
        string='Notes',
    )
    is_default = fields.Boolean(
        string='Default Task',
        default=False,
        help='Used as a template for new offboarding records',
    )
    sequence = fields.Integer(
        default=10,
    )

    def action_complete(self):
        """Mark task as completed."""
        for task in self:
            task.completed = True
            task.completed_date = fields.Date.today()

    def action_reset(self):
        """Reset task to incomplete."""
        for task in self:
            task.completed = False
            task.completed_date = False
