from odoo import fields, models, api, _
from odoo.exceptions import UserError


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    employment_status = fields.Selection(
        [('probation', 'Probation'),
         ('active', 'Active'),
         ('suspended', 'Suspended'),
         ('terminated', 'Terminated')],
        string='Employment Status',
        default='probation',
        tracking=True,
    )
    probation_end_date = fields.Date(
        string='Probation End Date',
        tracking=True,
    )
    notice_period_days = fields.Integer(
        string='Notice Period (Days)',
        default=30,
        help='Default notice period in days for this employee',
    )
    emergency_contact_name = fields.Char(
        string='Emergency Contact Name',
    )
    emergency_contact_phone = fields.Char(
        string='Emergency Contact Phone',
    )
    bank_account = fields.Char(
        string='Bank Account Number',
    )
    bank_sort_code = fields.Char(
        string='Bank Sort Code / Routing',
        help='UK sort code or international equivalent',
    )
    contract_ids = fields.One2many(
        'hr.lifecycle.contract',
        'employee_id',
        string='Contracts',
    )
    offboarding_ids = fields.One2many(
        'hr.offboarding',
        'employee_id',
        string='Offboarding Records',
    )

    def action_confirm_probation(self):
        """Move employee from probation to active status."""
        for employee in self:
            if employee.employment_status != 'probation':
                raise UserError(_(
                    'Employee "%s" is not in probation status.',
                    employee.name
                ))
            employee.employment_status = 'active'

    def action_terminate_employment(self):
        """Terminate employment."""
        for employee in self:
            if employee.employment_status == 'terminated':
                raise UserError(_(
                    'Employee "%s" is already terminated.',
                    employee.name
                ))
            employee.employment_status = 'terminated'

    @api.model
    def _cron_check_probation_end(self):
        """Cron job: auto-confirm probation when probation_end_date is reached."""
        today = fields.Date.today()
        employees = self.search([
            ('employment_status', '=', 'probation'),
            ('probation_end_date', '<=', today),
            ('probation_end_date', '!=', False),
        ])
        employees.action_confirm_probation()
