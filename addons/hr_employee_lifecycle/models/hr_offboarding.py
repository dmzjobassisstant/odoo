from odoo import fields, models, api, _
from odoo.exceptions import UserError


class HROffboarding(models.Model):
    _name = 'hr.offboarding'
    _description = 'Employee Offboarding'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(
        string='Reference',
        required=True,
        default='New',
        tracking=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        tracking=True,
        ondelete='restrict',
    )
    offboarding_type = fields.Selection(
        [('resignation', 'Resignation'),
         ('retirement', 'Retirement'),
         ('redundancy', 'Redundancy'),
         ('dismissal', 'Dismissal'),
         ('end_of_contract', 'End of Contract')],
        string='Offboarding Type',
        required=True,
        tracking=True,
    )
    initiated_by = fields.Selection(
        [('employee', 'Employee'),
         ('employer', 'Employer')],
        string='Initiated By',
        required=True,
        tracking=True,
    )
    reason = fields.Text(
        string='Reason',
        tracking=True,
    )
    notice_given_date = fields.Date(
        string='Notice Given Date',
        tracking=True,
    )
    last_working_date = fields.Date(
        string='Last Working Date',
        tracking=True,
    )
    settlement_amount = fields.Float(
        string='Settlement Amount',
        tracking=True,
    )
    settlement_breakdown = fields.Text(
        string='Settlement Breakdown',
        help='Detailed breakdown of the settlement calculation',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('in_progress', 'In Progress'),
         ('completed', 'Completed'),
         ('cancelled', 'Cancelled')],
        string='Status',
        default='draft',
        tracking=True,
    )
    task_ids = fields.One2many(
        'hr.offboarding.task',
        'offboarding_id',
        string='Offboarding Tasks',
        copy=True,
    )
    contract_id = fields.Many2one(
        'hr.lifecycle.contract',
        string='Related Contract',
        domain="[('employee_id', '=', employee_id)]",
    )
    employee_status = fields.Selection(
        related='employee_id.employment_status',
        string='Employee Status',
        readonly=True,
    )
    department_id = fields.Many2one(
        related='employee_id.department_id',
        string='Department',
        readonly=True,
    )
    training_plan_ids = fields.Many2many(
        'training.plan', 'offboarding_training_plan_rel',
        'offboarding_id', 'plan_id',
        string='Training Plans',
        help='Training plans to assign to the employee during offboarding.',
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'hr.offboarding'
                ) or 'New'
        return super().create(vals_list)

    def action_start(self):
        """Move offboarding from draft to in_progress."""
        for record in self:
            if record.state != 'draft':
                raise UserError(_(
                    'Only draft offboarding records can be started.'
                ))
            record.state = 'in_progress'
            # Create default tasks if none exist
            if not record.task_ids:
                default_tasks = self.env['hr.offboarding.task'].search([
                    ('is_default', '=', True),
                ])
                for task_tmpl in default_tasks:
                    self.env['hr.offboarding.task'].create({
                        'offboarding_id': record.id,
                        'name': task_tmpl.name,
                        'assigned_to': task_tmpl.assigned_to.id,
                    })
            # Auto-create training assignments from linked plans
            if record.training_plan_ids:
                Assignment = self.env.get('training.assignment')
                if Assignment:
                    for plan in record.training_plan_ids:
                        for course in plan.course_ids:
                            existing = Assignment.search([
                                ('employee_id', '=', record.employee_id.id),
                                ('course_id', '=', course.id),
                            ])
                            if not existing:
                                Assignment.create({
                                    'employee_id': record.employee_id.id,
                                    'course_id': course.id,
                                    'assigned_by': record.employee_id.id,
                                    'assigned_date': fields.Date.today(),
                                    'state': 'assigned',
                                })
        return True

    def action_complete(self):
        """Complete the offboarding process."""
        for record in self:
            if record.state != 'in_progress':
                raise UserError(_(
                    'Only in-progress offboarding records can be completed.'
                ))
            incomplete = record.task_ids.filtered(lambda t: not t.completed)
            if incomplete:
                raise UserError(_(
                    'All offboarding tasks must be completed before '
                    'marking the offboarding as complete. '
                    'Incomplete tasks: %s'
                ) % ', '.join(incomplete.mapped('name')))
            record.state = 'completed'
            record.employee_id.employment_status = 'terminated'
            if record.contract_id and record.contract_id.state == 'active':
                record.contract_id.state = 'terminated'
        return True

    def action_cancel(self):
        """Cancel the offboarding process."""
        for record in self:
            if record.state == 'completed':
                raise UserError(_(
                    'Completed offboarding records cannot be cancelled.'
                ))
            record.state = 'cancelled'
        return True

    def action_reset_to_draft(self):
        """Reset completed offboarding back to draft."""
        for record in self:
            if record.state != 'completed':
                raise UserError(_(
                    'Only completed offboarding records can be reset.'
                ))
            record.state = 'draft'
        return True

    @api.onchange('offboarding_type', 'contract_id')
    def _onchange_calculate_settlement(self):
        """Auto-calculate settlement for redundancy based on contract data."""
        if self.offboarding_type == 'redundancy' and self.contract_id:
            contract = self.contract_id
            if contract.statutory_redundancy_weeks and contract.wage:
                weekly_pay = contract.wage / 4.33
                self.settlement_amount = (
                    weekly_pay * contract.statutory_redundancy_weeks
                )
                self.settlement_breakdown = (
                    'Weekly pay: %.2f (Wage %.2f / 4.33) × %s weeks\n'
                    'Total: %.2f'
                ) % (
                    weekly_pay, contract.wage,
                    contract.statutory_redundancy_weeks,
                    self.settlement_amount,
                )
