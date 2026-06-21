from odoo import models, fields


class TrainingCompletion(models.Model):
    _name = 'training.completion'
    _description = 'Training Completion'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'completed_date desc'

    assignment_id = fields.Many2one(
        'training.assignment', string='Assignment',
        ondelete='cascade', required=True,
    )
    employee_id = fields.Many2one(
        'hr.employee', string='Employee',
        required=True,
    )
    course_id = fields.Many2one(
        'training.course', string='Course',
        required=True,
    )
    completed_date = fields.Date(
        string='Completed Date',
        default=fields.Date.today,
    )
    score = fields.Float(string='Score')
    certificate = fields.Binary(
        string='Certificate',
        attachment=True,
    )
