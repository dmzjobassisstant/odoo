from odoo import models, fields


class TrainingPlan(models.Model):
    _name = 'training.plan'
    _description = 'Training Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(required=True, tracking=True)
    description = fields.Html()
    category = fields.Selection(
        [('onboarding', 'Onboarding'),
         ('compliance', 'Compliance'),
         ('technical', 'Technical'),
         ('soft_skills', 'Soft Skills'),
         ('safety', 'Safety')],
        string='Category',
        tracking=True,
    )
    course_ids = fields.One2many('training.course', 'plan_id', string='Courses')
    required_for_roles = fields.Many2many('hr.job', string='Required for Roles')
    active = fields.Boolean(default=True, tracking=True)
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
    )
