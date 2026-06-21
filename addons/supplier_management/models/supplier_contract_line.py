# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SupplierContractLine(models.Model):
    _name = 'supplier.contract.line'
    _description = 'Supplier Contract Line'
    _order = 'id'

    contract_id = fields.Many2one(
        'supplier.contract', string='Contract',
        required=True, ondelete='cascade',
        index=True,
    )
    product_id = fields.Many2one(
        'product.product', string='Product',
        domain="[('purchase_ok', '=', True)]",
    )
    description = fields.Char(string='Description')
    quantity = fields.Float(string='Quantity', default=1.0, required=True)
    unit_price = fields.Float(string='Unit Price', required=True, digits='Product Price')
    tax_id = fields.Many2one(
        'account.tax', string='Tax',
        domain="[('type_tax_use', '=', 'purchase')]",
        help='Tax applied to this line',
    )
    currency_id = fields.Many2one('res.currency', related='contract_id.currency_id')
    company_id = fields.Many2one('res.company', related='contract_id.company_id')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.unit_price
