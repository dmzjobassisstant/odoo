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

    # --- Per-assignment competency level overrides ---
    competency_level_ids = fields.One2many(
        'competency.project.assignment.competency', 'assignment_id',
        string='Competency Levels'
    )

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

    @api.onchange('role_id')
    def _onchange_role_id(self):
        """Auto-populate competency lines from role's required competencies."""
        if not self.role_id:
            self.competency_level_ids = [(5, 0, 0)]
            return
        required = self.role_id.role_competency_ids
        lines = []
        for seq, rc in enumerate(required):
            lines.append((0, 0, {
                'competency_id': rc.competency_id.id,
                'required_level_id': rc.required_level_id.id,
                'sequence': seq * 10,
            }))
        self.competency_level_ids = [(5, 0, 0)] + lines

    @api.onchange('employee_id', 'competency_level_ids')
    def _onchange_trigger_gap(self):
        """Recalculate gap analysis in the UI when employee or levels change."""
        self._compute_gap()

    def action_analyze_gap(self):
        """Force-recalculate gap analysis for selected role assignments."""
        self._compute_gap()
        # Force the parent assessment to refresh
        self.mapped('assessment_id')._compute_gap()
        return {'type': 'ir.actions.client', 'tag': 'reload'}

    @api.depends('role_id', 'employee_id', 'competency_level_ids.required_level_id')
    def _compute_gap(self):
        for rec in self:
            if not rec.role_id or not rec.employee_id:
                rec.required_competency_count = 0
                rec.met_competency_count = 0
                rec.missing_competency_count = 0
                rec.below_level_count = 0
                rec.gap_status = 'missing'
                continue

            # Use per-assignment competency levels if populated, else role defaults
            if rec.competency_level_ids:
                required = rec.competency_level_ids
            else:
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
            for item in required:
                # Handle both model types
                if hasattr(item, 'competency_id'):
                    cid = item.competency_id.id
                    req_level = item.required_level_id
                else:
                    # role_competency_ids fallback
                    cid = item.competency_id.id
                    req_level = getattr(item, 'required_level_id', None)
                    if req_level is None:
                        continue

                if cid not in assessed:
                    missing += 1
                elif req_level and assessed[cid] and req_level.sequence > assessed[cid].sequence:
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


class CompetencyProjectAssignmentCompetency(models.Model):
    _name = 'competency.project.assignment.competency'
    _description = 'Project Assignment Competency Level'
    _order = 'sequence, id'

    assignment_id = fields.Many2one(
        'competency.project.role.assignment', required=True, ondelete='cascade')
    competency_id = fields.Many2one(
        'competency.competency', string='Competency', required=True)
    required_level_id = fields.Many2one(
        'competency.level', string='Required Level', required=True)
    sequence = fields.Integer(default=10)
