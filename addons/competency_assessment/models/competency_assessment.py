from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError
import json

class CompetencyAssessment(models.Model):
    _name = 'competency.assessment'
    _description = 'Competency Assessment'
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_employee(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)

    name = fields.Char(string='Reference', readonly=True, copy=False, default='New')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,
        default=_default_employee, tracking=True,
        help='The employee being assessed. Can only be changed in Draft state.')
    discipline_id = fields.Many2one('competency.discipline', string='Discipline',
        required=True, tracking=True,
        help='Select a discipline to auto-load its competencies. Can only be changed in Draft state.')
    lead_id = fields.Many2one('hr.employee', string='Discipline Lead',
        related='discipline_id.lead_id', store=True, readonly=True)
    approver_ids = fields.Many2many(
        'hr.employee', 'competency_assessment_approver_rel',
        'assessment_id', 'employee_id',
        string='Approvers',
        tracking=True,
        domain="[('department_id', '!=', False)]",
        help='Approvers who can review and confirm this assessment. The discipline lead is added by default.'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('self_assessed', 'Self-Assessed'),
        ('lead_reviewed', 'Lead Reviewed'),
        ('employee_accepted', 'Employee Accepted'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True, group_expand='_group_expand_states')

    assessment_date = fields.Date(default=fields.Date.today, tracking=True)
    line_ids = fields.One2many('competency.assessment.line', 'assessment_id', string='Assessment Lines')
    employee_acceptance_date = fields.Datetime(tracking=True)
    lead_confirmation_date = fields.Datetime(tracking=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    active = fields.Boolean(default=True)

    def _group_expand_states(self, states, domain, order):
        return [key for key, _ in self._fields['state'].selection]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('competency.assessment') or 'New'
        return super().create(vals_list)

    def write(self, vals):
        """Prevent changing employee/discipline after draft state."""
        for record in self:
            if record.state != 'draft':
                if 'employee_id' in vals:
                    raise UserError(_('Employee cannot be changed after the assessment leaves Draft state.'))
                if 'discipline_id' in vals:
                    raise UserError(_('Discipline cannot be changed after the assessment leaves Draft state.'))
        return super().write(vals)

    @api.onchange('discipline_id')
    def _onchange_discipline_id(self):
        """Auto-populate assessment lines with active competencies from the selected discipline."""
        if not self.discipline_id:
            return
        # Only auto-load in draft (new record or draft state)
        if self.state and self.state not in ('draft', False):
            return
        # Clear existing lines
        self.line_ids = [(5, 0, 0)]
        # Load active competencies from the discipline
        competencies = self.env['competency.competency'].search([
            ('discipline_id', '=', self.discipline_id.id),
            ('active', '=', True),
        ], order='sequence, name')
        if not competencies:
            return
        lines = []
        for comp in competencies:
            criteria_data = []
            for crit in comp.criterion_ids:
                criteria_data.append({
                    'level': crit.level_id.name,
                    'level_code': crit.level_id.code,
                    'description': crit.description,
                })
            criteria_json = json.dumps(criteria_data, indent=2) if criteria_data else '[]'
            lines.append((0, 0, {
                'competency_id': comp.id,
                'competency_name': comp.name,
                'competency_description': comp.description or '',
                'criteria_snapshot': criteria_json,
            }))
        self.line_ids = lines
        # Default approvers to the discipline lead
        if self.discipline_id.lead_id:
            self.approver_ids = [(4, self.discipline_id.lead_id.id)]

    def _is_approver(self):
        """Check if the current user is an approver or the discipline lead."""
        self.ensure_one()
        if self.env.user.has_group('competency_assessment.group_competency_admin'):
            return True
        if self.env.user.has_group('competency_assessment.group_discipline_lead'):
            if self.lead_id.user_id == self.env.user:
                return True
            if self.approver_ids.filtered(lambda a: a.user_id == self.env.user):
                return True
        return False

    def action_self_assess(self):
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('Assessment must be in Draft state to submit.'))
        if not self.line_ids:
            raise UserError(_('Please add at least one competency before submitting.'))
        self.state = 'self_assessed'
        self.message_post(body=_('Self-assessment submitted.'))

    def action_lead_review(self):
        self.ensure_one()
        if not self._is_approver():
            raise AccessError(_('Only designated approvers or the discipline lead can review this assessment.'))
        if self.state != 'self_assessed':
            raise UserError(_('Assessment must be in Self-Assessed state.'))
        # Require evaluations on all lines
        lines_without_eval = self.line_ids.filtered(lambda l: not l.lead_evaluation)
        if lines_without_eval:
            raise UserError(_(
                'Please set the Lead Evaluation (Competent / Not Competent) for all assessment lines '
                'before marking the review complete.\n\nLines missing evaluation: %s'
            ) % ', '.join(lines_without_eval.mapped('competency_name')))
        self.state = 'lead_reviewed'
        self.message_post(body=_('Lead review completed by %s.') % self.env.user.name)

    def action_employee_accept(self):
        self.ensure_one()
        if self.employee_id.user_id != self.env.user:
            raise AccessError(_('Only the assessed employee can accept.'))
        if self.state != 'lead_reviewed':
            raise UserError(_('Assessment must be lead-reviewed first.'))
        self.employee_acceptance_date = fields.Datetime.now()
        self.state = 'employee_accepted'
        self.message_post(body=_('Employee accepted the assessment.'))

    def action_lead_confirm(self):
        self.ensure_one()
        if not self._is_approver():
            raise AccessError(_('Only designated approvers or the discipline lead can confirm this assessment.'))
        if self.state != 'employee_accepted':
            raise UserError(_('Employee must accept before lead confirmation.'))
        self.lead_confirmation_date = fields.Datetime.now()
        self.state = 'done'
        self.message_post(body=_('Assessment confirmed by %s — recorded.') % self.env.user.name)

    def action_cancel(self):
        self.state = 'cancelled'

    def action_reset_draft(self):
        self.state = 'draft'


class CompetencyAssessmentLine(models.Model):
    _name = 'competency.assessment.line'
    _description = 'Assessment Line'
    _order = 'competency_id'

    assessment_id = fields.Many2one('competency.assessment', required=True, ondelete='cascade')
    state = fields.Selection(related='assessment_id.state', string='Assessment State', store=False)
    competency_id = fields.Many2one('competency.competency', string='Competency', readonly=True)
    competency_name = fields.Char(string='Competency (snapshot)', readonly=True)
    competency_description = fields.Text(string='Description (snapshot)', readonly=True)
    criteria_snapshot = fields.Text(string='Criteria (raw JSON)', readonly=True)
    criteria_display = fields.Text(string='Criteria', compute='_compute_criteria_display')
    self_assessed_level_id = fields.Many2one('competency.level', string='Self-Assessed Level',
        help='The level the employee believes they are at.')
    employee_comment = fields.Text(string='Employee Comment')
    lead_evaluation = fields.Selection([
        ('competent', 'Competent'),
        ('not_competent', 'Not Competent'),
    ], string='Lead Evaluation',
        help='Set by the approver during review.')
    lead_assigned_level_id = fields.Many2one('competency.level', string='Lead-Assigned Level',
        help='The level assigned by the approver.')
    lead_comment = fields.Text(string='Lead Comment')
    attachment_ids = fields.Many2many('ir.attachment', string='Evidence')
    sequence = fields.Integer(default=10)

    @api.depends('criteria_snapshot')
    def _compute_criteria_display(self):
        for line in self:
            if not line.criteria_snapshot:
                line.criteria_display = ''
                continue
            try:
                criteria = json.loads(line.criteria_snapshot)
                lines = []
                for c in criteria:
                    level = c.get('level', '?')
                    desc = c.get('description', '')
                    lines.append(f"• {level}: {desc}")
                line.criteria_display = '\n'.join(lines)
            except (json.JSONDecodeError, TypeError):
                line.criteria_display = line.criteria_snapshot

    def write(self, vals):
        """Restrict which fields can be edited based on the parent assessment state."""
        for line in self:
            parent_state = line.assessment_id.state

            if parent_state == 'draft':
                # Employee can set self-assessment fields
                blocked = {'lead_evaluation', 'lead_assigned_level_id', 'lead_comment'}
            elif parent_state == 'self_assessed':
                # Approver can set lead review fields
                blocked = {'self_assessed_level_id', 'employee_comment', 'attachment_ids'}
            else:
                # All fields locked in other states
                blocked = {'self_assessed_level_id', 'employee_comment', 'attachment_ids',
                           'lead_evaluation', 'lead_assigned_level_id', 'lead_comment'}

            illegal = set(vals.keys()) & blocked
            if illegal:
                raise UserError(_(
                    'The following fields cannot be modified when the assessment is in "%s" state: %s'
                ) % (parent_state, ', '.join(sorted(illegal))))

        return super().write(vals)
