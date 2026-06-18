from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CompetencyProjectAssessment(models.Model):
    _name = 'competency.project.assessment'
    _description = 'Project Competency Assessment'
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', readonly=True, copy=False, default='New')
    project_id = fields.Many2one('project.project', string='Project', required=True,
                                 tracking=True)
    description = fields.Text(tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True, group_expand='_group_expand_states')
    assessment_date = fields.Date(default=fields.Date.today, tracking=True)
    role_assignment_ids = fields.One2many(
        'competency.project.role.assignment', 'assessment_id',
        string='Role Assignments'
    )
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    active = fields.Boolean(default=True)

    def _group_expand_states(self, states, domain, order):
        return [key for key, _ in self._fields['state'].selection]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'competency.project.assessment') or 'New'
        return super().create(vals_list)

    def action_start(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_reset_draft(self):
        self.state = 'draft'


class CompetencyProjectRoleAssignment(models.Model):
    _name = 'competency.project.role.assignment'
    _description = 'Project Role Assignment'
    _order = 'role_id, employee_id'

    assessment_id = fields.Many2one(
        'competency.project.assessment', required=True, ondelete='cascade')
    role_id = fields.Many2one('competency.role', string='Role', required=True,
                              tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Person', required=True,
                                  tracking=True)
    assigned_date = fields.Date(default=fields.Date.today)
    notes = fields.Text()

    # --- Gap Analysis (computed) ---
    required_competency_count = fields.Integer(compute='_compute_gap', store=False)
    met_competency_count = fields.Integer(compute='_compute_gap', store=False)
    missing_competency_count = fields.Integer(compute='_compute_gap', store=False)
    below_level_count = fields.Integer(compute='_compute_gap', store=False)
    gap_status = fields.Selection([
        ('ok', 'All Met'),
        ('gaps', 'Has Gaps'),
        ('missing', 'Not Assessed'),
    ], compute='_compute_gap', store=False)

    def _get_employee_levels(self):
        """Return dict mapping competency_id -> highest assessed level."""
        self.ensure_one()
        if not self.employee_id:
            return {}
        lines = self.env['competency.assessment.line'].search([
            ('assessment_id.employee_id', '=', self.employee_id.id),
            ('assessment_id.state', '=', 'done'),
            ('competency_id', '!=', False),
        ])
        result = {}
        for line in lines:
            cid = line.competency_id.id
            if cid not in result:
                level = line.lead_assigned_level_id or line.self_assessed_level_id
                result[cid] = level
        return result

    @api.depends('role_id', 'employee_id', 'role_id.role_competency_ids')
    def _compute_gap(self):
        for rec in self:
            if not rec.role_id or not rec.employee_id:
                rec.required_competency_count = 0
                rec.met_competency_count = 0
                rec.missing_competency_count = 0
                rec.below_level_count = 0
                rec.gap_status = 'missing'
                continue

            required = rec.role_id.role_competency_ids
            rec.required_competency_count = len(required)
            if not required:
                rec.met_competency_count = 0
                rec.missing_competency_count = 0
                rec.below_level_count = 0
                rec.gap_status = 'ok'
                continue

            assessed = rec._get_employee_levels()
            met = missing = below = 0
            for rc in required:
                cid = rc.competency_id.id
                if cid not in assessed:
                    missing += 1
                elif rc.required_level_id.sequence > assessed[cid].sequence:
                    below += 1
                else:
                    met += 1

            rec.met_competency_count = met
            rec.missing_competency_count = missing
            rec.below_level_count = below
            if missing == 0 and below == 0:
                rec.gap_status = 'ok'
            elif met == 0 and below == 0:
                rec.gap_status = 'missing'
            else:
                rec.gap_status = 'gaps'
