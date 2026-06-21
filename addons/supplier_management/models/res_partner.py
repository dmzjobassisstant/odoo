# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    supplier_rating = fields.Selection(
        [('A', 'A - Excellent'), ('B', 'B - Good'), ('C', 'C - Average'), ('D', 'D - Poor')],
        string='Supplier Rating',
        tracking=True,
    )
    payment_terms_days = fields.Integer(
        string='Payment Terms (Days)',
        help='Default payment terms in days for this supplier',
    )
    bank_account = fields.Char(string='Bank Account Number')
    bank_sort_code = fields.Char(string='Sort Code')
    bank_iban = fields.Char(string='IBAN')
    direct_debit_mandate_ref = fields.Char(string='Direct Debit Mandate Reference')
    direct_debit_active = fields.Boolean(string='Direct Debit Active')
    contract_ids = fields.One2many(
        'supplier.contract', 'partner_id',
        string='Supplier Contracts',
        domain=[('state', '!=', 'cancelled')],
    )
    contract_count = fields.Integer(
        string='Contract Count',
        compute='_compute_contract_count',
    )

    @api.depends('contract_ids')
    def _compute_contract_count(self):
        for partner in self:
            partner.contract_count = len(partner.contract_ids)

    def action_view_supplier_contracts(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Supplier Contracts'),
            'res_model': 'supplier.contract',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)],
            'context': {'default_partner_id': self.id},
        }
