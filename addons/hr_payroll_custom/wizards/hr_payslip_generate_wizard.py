from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, timedelta


class HRPayslipGenerateWizard(models.TransientModel):
    _name = 'hr.payslip.generate.wizard'
    _description = 'Generate Payslip Wizard'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    contract_id = fields.Many2one('hr.lifecycle.contract', string='Contract',
                                   domain="[('employee_id', '=', employee_id), ('state', '=', 'active')]")
    period_start = fields.Date(string='Period Start', required=True,
                                default=lambda self: self._default_period_start())
    period_end = fields.Date(string='Period End', required=True,
                              default=lambda self: self._default_period_end())

    @api.model
    def _default_period_start(self):
        today = date.today()
        return date(today.year, today.month, 1)

    @api.model
    def _default_period_end(self):
        today = date.today()
        # Last day of current month
        next_month = today.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            active_contract = self.env['hr.lifecycle.contract'].search([
                ('employee_id', '=', self.employee_id.id),
                ('state', '=', 'active'),
            ], limit=1)
            self.contract_id = active_contract.id if active_contract else False

    def action_generate(self):
        """Generate a payslip for the selected employee and period."""
        self.ensure_one()

        if self.period_end < self.period_start:
            raise UserError(_('Period end date cannot be before period start date.'))

        # Check for duplicate
        existing = self.env['hr.payslip'].search([
            ('employee_id', '=', self.employee_id.id),
            ('period_start', '=', self.period_start),
            ('period_end', '=', self.period_end),
        ], limit=1)
        if existing:
            raise UserError(_(
                'A payslip already exists for %(employee)s for period %(start)s to %(end)s.'
            ) % {
                'employee': self.employee_id.name,
                'start': self.period_start,
                'end': self.period_end,
            })

        # Create the payslip
        payslip = self.env['hr.payslip'].create({
            'employee_id': self.employee_id.id,
            'contract_id': self.contract_id.id,
            'period_start': self.period_start,
            'period_end': self.period_end,
        })

        # Generate lines
        payslip.action_generate_lines()

        # Return action to open the payslip
        return {
            'type': 'ir.actions.act_window',
            'name': _('Payslip'),
            'res_model': 'hr.payslip',
            'res_id': payslip.id,
            'view_mode': 'form',
            'target': 'current',
        }
