from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HRPayslipLine(models.Model):
    _name = 'hr.payslip.line'
    _description = 'Payslip Line'
    _order = 'category, sequence, id'

    payslip_id = fields.Many2one('hr.payslip', string='Payslip', required=True,
                                  ondelete='cascade', index=True)
    name = fields.Char(string='Description', required=True)
    category = fields.Selection([
        ('earning', 'Earning'),
        ('deduction', 'Deduction'),
    ], string='Category', required=True)
    amount = fields.Float(string='Amount', required=True, default=0.0)
    sequence = fields.Integer(string='Sequence', default=10)
    company_id = fields.Many2one('res.company', string='Company',
                                  related='payslip_id.company_id', store=True)
