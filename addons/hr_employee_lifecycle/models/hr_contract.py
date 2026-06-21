from odoo import fields, models, api, _
from odoo.exceptions import UserError


class HRContract(models.Model):
    _name = 'hr.lifecycle.contract'
    _description = 'Employee Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_start desc'

    name = fields.Char(
        string='Contract Reference',
        required=True,
        tracking=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        tracking=True,
        ondelete='restrict',
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department',
        related='employee_id.department_id',
        store=True,
        readonly=False,
    )
    job_id = fields.Many2one(
        'hr.job',
        string='Job Position',
        related='employee_id.job_id',
        store=True,
        readonly=False,
    )
    contract_type = fields.Selection(
        [('permanent', 'Permanent'),
         ('fixed_term', 'Fixed Term'),
         ('contractor', 'Contractor'),
         ('zero_hours', 'Zero Hours')],
        string='Contract Type',
        default='permanent',
        required=True,
        tracking=True,
    )
    date_start = fields.Date(
        string='Start Date',
        required=True,
        tracking=True,
    )
    date_end = fields.Date(
        string='End Date',
        tracking=True,
        help='End date for fixed term contracts',
    )
    wage = fields.Float(
        string='Wage',
        required=True,
        tracking=True,
    )
    salary_breakdown = fields.Text(
        string='Salary Breakdown',
        help='Structured breakdown of pay components',
    )
    benefits = fields.Text(
        string='Benefits',
        help='List of employee benefits',
    )
    notice_period_employer_days = fields.Integer(
        string='Employer Notice Period (Days)',
        default=30,
        tracking=True,
    )
    notice_period_employee_days = fields.Integer(
        string='Employee Notice Period (Days)',
        default=30,
        tracking=True,
    )
    statutory_redundancy_weeks = fields.Float(
        string='Statutory Redundancy (Weeks)',
        default=0.0,
        tracking=True,
        help='Number of weeks of statutory redundancy pay entitlement',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('expired', 'Expired'),
         ('terminated', 'Terminated')],
        string='Status',
        default='draft',
        tracking=True,
    )
    notes = fields.Text(
        string='Notes',
    )

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for contract in self:
            if contract.date_end and contract.date_end < contract.date_start:
                raise UserError(_(
                    'Contract end date cannot be before start date.'
                ))

    def action_activate(self):
        """Activate the contract."""
        for contract in self:
            if contract.state not in ('draft', 'expired'):
                raise UserError(_(
                    'Contract "%s" can only be activated from draft or expired state.',
                    contract.name
                ))
            contract.state = 'active'
            # Also update the employee's status if in probation
            if contract.employee_id.employment_status == 'probation':
                contract.employee_id.employment_status = 'active'

    def action_terminate(self):
        """Terminate the contract."""
        for contract in self:
            if contract.state == 'terminated':
                raise UserError(_(
                    'Contract "%s" is already terminated.',
                    contract.name
                ))
            contract.state = 'terminated'

    def action_expire(self):
        """Set contract as expired (for fixed term)."""
        for contract in self:
            if contract.state == 'expired':
                raise UserError(_(
                    'Contract "%s" is already expired.',
                    contract.name
                ))
            contract.state = 'expired'
