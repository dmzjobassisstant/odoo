from odoo import models, fields, api

class CompetencyDiscipline(models.Model):
    _name = 'competency.discipline'
    _description = 'Competency Discipline'
    _order = 'sequence, name'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(string='Code', tracking=True)
    description = fields.Text(tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    sequence = fields.Integer(default=10)
    lead_id = fields.Many2one(
        'hr.employee', string='Discipline Lead',
        domain="[('department_id', '!=', False)]",
        tracking=True,
        help='The discipline lead is responsible for confirming competency assessments.'
    )
    competency_ids = fields.One2many('competency.competency', 'discipline_id', string='Competencies')
    competency_count = fields.Integer(compute='_compute_competency_count', store=True)
    assessment_ids = fields.One2many('competency.assessment', 'discipline_id', string='Assessments')

    @api.depends('competency_ids')
    def _compute_competency_count(self):
        for rec in self:
            rec.competency_count = len(rec.competency_ids)

class CompetencyLevel(models.Model):
    _name = 'competency.level'
    _description = 'Competency Proficiency Level'
    _order = 'sequence, name'

    name = fields.Char(required=True)
    code = fields.Char()
    sequence = fields.Integer(default=10)
    description = fields.Text()
    active = fields.Boolean(default=True)

class Competency(models.Model):
    _name = 'competency.competency'
    _description = 'Competency'
    _order = 'discipline_id, sequence, name'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, tracking=True)
    competency_code = fields.Char(string='Competency ID', tracking=True)
    description = fields.Text(tracking=True)
    discipline_id = fields.Many2one('competency.discipline', required=True, ondelete='cascade', tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    sequence = fields.Integer(default=10)
    criterion_ids = fields.One2many('competency.criterion', 'competency_id', string='Level Criteria')
    criterion_count = fields.Integer(compute='_compute_criterion_count', store=True)

    @api.depends('criterion_ids')
    def _compute_criterion_count(self):
        for rec in self:
            rec.criterion_count = len(rec.criterion_ids)

class CompetencyCriterion(models.Model):
    _name = 'competency.criterion'
    _description = 'Competency Level Criterion'
    _order = 'competency_id, level_id'

    competency_id = fields.Many2one('competency.competency', required=True, ondelete='cascade')
    level_id = fields.Many2one('competency.level', required=True, ondelete='restrict')
    description = fields.Text(required=True, string='Criterion Description')
    sequence = fields.Integer(default=10)
