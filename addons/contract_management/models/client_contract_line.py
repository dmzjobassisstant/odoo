from odoo import api, fields, models


class ClientContractLine(models.Model):
    _name = 'client.contract.line'
    _description = 'Client Contract Line'
    _order = 'id'

    contract_id = fields.Many2one(
        'client.contract',
        string='Contract',
        required=True,
        ondelete='cascade',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    description = fields.Char(
        string='Description',
    )
    quantity = fields.Float(
        string='Quantity',
        default=1.0,
        required=True,
    )
    unit_price = fields.Float(
        string='Unit Price',
        default=0.0,
        required=True,
    )
    tax_id = fields.Many2one(
        'account.tax',
        string='Tax',
    )
    service_code = fields.Char(
        string='Service Code',
    )
    company_id = fields.Many2one(
        'res.company',
        related='contract_id.company_id',
        store=False,
    )
    currency_id = fields.Many2one(
        'res.currency',
        related='contract_id.currency_id',
        store=False,
    )
    price_subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_price_subtotal',
    )

    @api.depends('quantity', 'unit_price')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * line.unit_price
