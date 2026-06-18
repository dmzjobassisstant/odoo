from odoo import models, fields, api, _
from odoo.exceptions import UserError
import json


class CompetencyProjectAssessment(models.Model):
    _name = 'competency.project.assessment'
    _description = 'Project Competency Assessment'
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', readonly=True, copy=False, default='New')
    project_id = fields.Many2one('project.project', string='Project', required=True, tracking=True)
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

    def action_gap_analysis(self):
        """Return a wizard or view showing the gap analysis for all role assignments."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Gap Analysis: %s') % self.name,
            'res_model': 'competency.project.role.assignment',
            'view_mode': 'list,form',
            'domain': [('assessment_id', '=', self.id)],
            'target': 'current',
            'context': {'gap_analysis_mode': True},
        }


class CompetencyProjectRoleAssignment(models.Model):
    _name = 'competency.project.role.assignment'
    _description = 'Project Role Assignment'
    _order = 'role_id, employee_id'

    assessment_id = fields.Many2one(
        'competency.project.assessment', required=True, ondelete='cascade')
    role_id = fields.Many2one('competency.role', string='Role', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Person', required=True, tracking=True)
    assigned_date = fields.Date(default=fields.Date.today)
    notes = fields.Text()

    # --- Gap Analysis Fields (computed) ---
    required_competency_count = fields.Integer(
        compute='_compute_gap_analysis', store=False)
    met_competency_count = fields.Integer(
        compute='_compute_gap_analysis', store=False)
    missing_competency_count = fields.Integer(
        compute='_compute_gap_analysis', store=False)
    below_level_count = fields.Integer(
        compute='_compute_gap_analysis', store=False)
    gap_status = fields.Selection([
        ('ok', 'All Met'),
        ('gaps', 'Has Gaps'),
        ('missing', 'Not Assessed'),
    ], compute='_compute_gap_analysis', store=False)
    gap_detail_ids = fields.One2many(
        'competency.gap.detail', 'assignment_id',
        string='Gap Details', compute='_compute_gap_detail', store=False)

    def _get_employee_assessed_levels(self):
        """Return dict mapping competency_id -> highest assessed level."""
        self.ensure_one()
        if not self.employee_id:
            return {}
        # Find the latest DONE assessment for this employee
        # per competency, use the lead_assigned_level (or self_assessed if no lead)
        lines = self.env['competency.assessment.line'].search([
            ('assessment_id.employee_id', '=', self.employee_id.id),
            ('assessment_id.state', '=', 'done'),
            ('competency_id', '!=', False),
        ])
        result = {}
        for line in lines:
            cid = line.competency_id.id
            if cid not in result:
                # Prefer lead-assigned level over self-assessed
                level = line.lead_assigned_level_id or line.self_assessed_level_id
                result[cid] = level
        return result

    @api.depends('role_id', 'employee_id', 'role_id.role_competency_ids')
    def _compute_gap_analysis(self):
        for assignment in self:
            if not assignment.role_id or not assignment.employee_id:
                assignment.required_competency_count = 0
                assignment.met_competency_count = 0
                assignment.missing_competency_count = 0
                assignment.below_level_count = 0
                assignment.gap_status = 'missing'
                continue

            required = assignment.role_id.role_competency_ids
            assignment.required_competency_count = len(required)
            if not required:
                assignment.met_competency_count = 0
                assignment.missing_competency_count = 0
                assignment.below_level_count = 0
                assignment.gap_status = 'ok'
                continue

            assessed = assignment._get_employee_assessed_levels()

            met = 0
            missing = 0
            below = 0
            for rc in required:
                if rc.competency_id.id not in assessed:
                    missing += 1
                elif rc.required_level_id.sequence > assessed[rc.competency_id.id].sequence:
                    below += 1
                else:
                    met += 1

            assignment.met_competency_count = met
            assignment.missing_competency_count = missing
            assignment.below_level_count = below
            if missing == 0 and below == 0:
                assignment.gap_status = 'ok'
            elif met == 0 and below == 0:
                assignment.gap_status = 'missing'
            else:
                assignment.gap_status = 'gaps'

    def _compute_gap_detail(self):
        """Compute per-competency gap details for display."""
        for assignment in self:
            if not assignment.role_id or not assignment.employee_id:
                assignment.gap_detail_ids = []
                continue
            assessed = assignment._get_employee_assessed_levels()
            details = []
            for rc in assignment.role_id.role_competency_ids:
                cid = rc.competency_id.id
                emp_level = assessed.get(cid)
                details.append({
                    'assignment_id': assignment.id,
                    'competency_name': rc.competency_id.name,
                    'required_level_name': rc.required_level_id.name,
                    'employee_level_name': emp_level.name if emp_level else 'Not assessed',
                    'gap_type': 'ok' if emp_level and emp_level.sequence >= rc.required_level_id.sequence
                        else 'below' if emp_level else 'missing',
                })
            assignment.gap_detail_ids = [(5, 0, 0)] + [
                (0, 0, d) for d in details
            ]


class CompetencyGapDetail(models.TransientModel):
    _name = 'competency.gap.detail'
    _description = 'Gap Analysis Detail (Transient)'

    assignment_id = fields.Many2one('competency.project.role.assignment', required=True)
    competency_name = fields.Char(string='Competency', readonly=True)
    required_level_name = fields.Char(string='Required Level', readonly=True)
    employee_level_name = fields.Char(string='Employee Level', readonly=True)
    gap_type = fields.Selection([
        ('ok', '✓ Meets Requirements'),
        ('below', '⚠ Below Required'),
        ('missing', '✗ Not Assessed'),
    ], string='Status', readonly=True)
