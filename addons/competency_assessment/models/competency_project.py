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

    # Aggregate gap counts across all role assignments
    total_gaps = fields.Integer(compute='_compute_summary', store=False)
    total_assignments = fields.Integer(compute='_compute_summary', store=False)
    assignments_with_gaps = fields.Integer(compute='_compute_summary', store=False)

    def _compute_summary(self):
        for rec in self:
            rec.total_assignments = len(rec.role_assignment_ids)
            rec.total_gaps = sum(a.missing_competency_count + a.below_level_count
                                 for a in rec.role_assignment_ids)
            rec.assignments_with_gaps = sum(
                1 for a in rec.role_assignment_ids if a.gap_status in ('gaps', 'missing'))

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

    def action_analyze_all_gaps(self):
        """Force-recalculate gap analysis for all role assignments."""
        for assignment in self.role_assignment_ids:
            assignment._compute_gap_detail()
        return {'type': 'ir.actions.client', 'tag': 'reload'}


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
        """Return dict mapping competency_id -> {'level', 'assessment_date', 'assessment_ref'}
        for the employee's latest assessment per competency.
        Falls back to competency_name matching if competency_id is not set."""
        self.ensure_one()
        if not self.employee_id:
            return {}
        # Get all completed/in-progress assessment lines for this employee
        lines = self.env['competency.assessment.line'].search([
            ('assessment_id.employee_id', '=', self.employee_id.id),
            ('assessment_id.state', 'in', ('done', 'employee_accepted', 'lead_reviewed', 'self_assessed')),
        ])
        # Sort by assessment create_date (newest first)
        lines = lines.sorted(key=lambda l: l.assessment_id.create_date, reverse=True)
        
        # Build a name→id lookup from active competencies
        competencies = self.env['competency.competency'].search([('active', '=', True)])
        name_to_id = {c.name: c.id for c in competencies}
        
        result = {}
        for line in lines:
            # Resolve competency_id — prefer direct FK, fall back to name match
            cid = line.competency_id.id if line.competency_id else None
            if not cid and line.competency_name:
                cid = name_to_id.get(line.competency_name)
            
            if not cid:
                continue  # Can't resolve
            
            if cid not in result:
                # First (newest) assessment for this competency wins
                level = line.lead_assigned_level_id or line.self_assessed_level_id
                result[cid] = {
                    'level': level,
                    'assessment_date': line.assessment_id.assessment_date,
                    'assessment_ref': line.assessment_id.name,
                }
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
        """Force-recalculate gap analysis and per-competency detail."""
        self._compute_gap()
        self._compute_gap_detail()
        return {'type': 'ir.actions.client', 'tag': 'reload'}

    @api.depends('role_id', 'employee_id', 'competency_level_ids.required_level_id',
                 'competency_level_ids.competency_id')
    def _compute_gap(self):
        """Compute aggregate gap counts."""
        for rec in self:
            if not rec.role_id or not rec.employee_id:
                rec.required_competency_count = 0
                rec.met_competency_count = 0
                rec.missing_competency_count = 0
                rec.below_level_count = 0
                rec.gap_status = 'missing'
                continue

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
                if hasattr(item, 'competency_id'):
                    cid = item.competency_id.id
                    req_level = item.required_level_id
                else:
                    cid = item.competency_id.id
                    req_level = getattr(item, 'required_level_id', None)
                    if req_level is None:
                        continue

                if cid not in assessed:
                    missing += 1
                else:
                    emp_data = assessed[cid]
                    emp_level = emp_data.get('level')
                    if req_level and emp_level and req_level.sequence > emp_level.sequence:
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

    def _compute_gap_detail(self):
        """Populate per-competency gap detail on competency_level_ids lines.
        Auto-triggered when employee or role changes."""
        for rec in self:
            if not rec.employee_id or not rec.competency_level_ids:
                continue
            assessed = rec._get_employee_levels()
            for comp_line in rec.competency_level_ids:
                cid = comp_line.competency_id.id
                if cid in assessed:
                    emp_data = assessed[cid]
                    emp_level = emp_data.get('level')
                    comp_line.employee_level_id = emp_level.id if emp_level else False
                    comp_line.assessment_ref = emp_data.get('assessment_ref', '')
                else:
                    comp_line.employee_level_id = False
                    comp_line.assessment_ref = ''

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._compute_gap_detail()
        return records

    def write(self, vals):
        result = super().write(vals)
        if 'employee_id' in vals or 'role_id' in vals:
            self._compute_gap_detail()
        return result


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

    # Employee's current assessed level (populated by gap analysis)
    employee_level_id = fields.Many2one(
        'competency.level', string='Employee Level',
        readonly=True,
        help='Employee\'s latest assessed level for this competency.')
    assessment_ref = fields.Char(
        string='Source Assessment', readonly=True,
        help='Reference of the assessment this level came from.')

    # Computed gap indicator
    is_gap = fields.Boolean(compute='_compute_is_gap', store=False, string='Gap')
    gap_summary = fields.Char(compute='_compute_is_gap', store=False, string='Gap Detail')

    # Coverage plan for gaps
    is_coverage_needed = fields.Boolean(
        string='Coverage Needed',
        help='Check if a coverage/action plan is needed for this competency gap.')
    coverage_plan = fields.Text(
        string='Coverage / Action Plan',
        help='Describe how management plans to cover this competency gap '
             '(e.g., training, mentoring, reassignment, external hire).')
    coverage_status = fields.Selection([
        ('open', 'Open'),
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ], string='Coverage Status', default='open')
    coverage_target_date = fields.Date(string='Target Date')

    sequence = fields.Integer(default=10)

    @api.depends('required_level_id', 'employee_level_id')
    def _compute_is_gap(self):
        for rec in self:
            if not rec.employee_level_id or not rec.required_level_id:
                rec.is_gap = False
                rec.gap_summary = '— Not assessed'
            elif rec.required_level_id.sequence > rec.employee_level_id.sequence:
                rec.is_gap = True
                rec.gap_summary = (
                    f'{rec.employee_level_id.name} ➔ {rec.required_level_id.name}'
                )
            else:
                rec.is_gap = False
                rec.gap_summary = (
                    f'{rec.employee_level_id.name} ≥ {rec.required_level_id.name}'
                )
