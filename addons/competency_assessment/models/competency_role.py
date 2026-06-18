from odoo import models, fields, api, _


class CompetencyRole(models.Model):
    _name = 'competency.role'
    _description = 'Competency Role'
    _order = 'sequence, name'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(tracking=True)
    description = fields.Text(tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    sequence = fields.Integer(default=10)
    discipline_id = fields.Many2one(
        'competency.discipline', string='Discipline',
        tracking=True,
        help='Optionally scope this role to a specific discipline.'
    )
    role_competency_ids = fields.One2many(
        'competency.role.competency', 'role_id',
        string='Required Competencies'
    )
    competency_count = fields.Integer(compute='_compute_competency_count', store=True)

    @api.depends('role_competency_ids')
    def _compute_competency_count(self):
        for rec in self:
            rec.competency_count = len(rec.role_competency_ids)


class CompetencyRoleCompetency(models.Model):
    _name = 'competency.role.competency'
    _description = 'Role Required Competency'
    _order = 'role_id, sequence'

    role_id = fields.Many2one('competency.role', required=True, ondelete='cascade')
    competency_id = fields.Many2one('competency.competency', string='Competency',
                                    required=True, tracking=True)
    required_level_id = fields.Many2one('competency.level', string='Required Level',
                                        required=True, tracking=True)
    notes = fields.Text(string='Notes')
    sequence = fields.Integer(default=10)

    @api.onchange('role_id')
    def _onchange_role_id(self):
        if self.role_id and self.role_id.discipline_id:
            return {'domain': {'competency_id': [
                ('discipline_id', '=', self.role_id.discipline_id.id),
                ('active', '=', True),
            ]}}
        return {'domain': {'competency_id': [('active', '=', True)]}}
