from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, timedelta


class HRSalaryRule(models.Model):
    _name = 'hr.salary.rule'
    _description = 'Salary Rule'
    _order = 'category, sequence, name'

    name = fields.Char(string='Name', required=True, translate=True)
    code = fields.Char(string='Code', required=True,
                       help='Unique identifier for this rule (e.g. BASIC, NI, TAX)')
    category = fields.Selection([
        ('earning', 'Earning'),
        ('deduction', 'Deduction'),
    ], string='Category', required=True, default='earning')
    rate_type = fields.Selection([
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
    ], string='Rate Type', required=True, default='percentage')
    rate_value = fields.Float(string='Rate Value', required=True, default=0.0,
                               help='Percentage (e.g. 20.0 for 20%) or fixed amount')
    applies_to_all = fields.Boolean(string='Apply to All Payslips', default=False,
                                     help='If checked, this rule is auto-applied when generating any payslip')
    sequence = fields.Integer(string='Sequence', default=10)
    company_id = fields.Many2one('res.company', string='Company',
                                  default=lambda self: self.env.company)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code, company_id)',
         'Salary rule code must be unique per company!'),
    ]
