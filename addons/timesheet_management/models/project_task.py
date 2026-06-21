from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    timesheet_entry_ids = fields.One2many(
        'timesheet.entry',
        'task_id',
        string='Timesheet Entries',
    )
