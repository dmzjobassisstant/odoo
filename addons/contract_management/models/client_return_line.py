from odoo import api, fields, models


class ClientReturnLine(models.Model):
    _name = 'client.return.line'
    _description = 'Client Return Line'
    _order = 'id'

    return_id = fields.Many2one(
        'client.return',
        string='Return',
        required=True,
        ondelete='cascade',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
    )
    quantity = fields.Float(
        string='Quantity',
        default=1.0,
        required=True,
    )
    reason = fields.Text(
        string='Reason',
    )
    state = fields.Selection(
        [
            ('pending', 'Pending'),
            ('received', 'Received'),
            ('inspected', 'Inspected'),
            ('refunded', 'Refunded'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='pending',
        required=True,
    )
    company_id = fields.Many2one(
        'res.company',
        related='return_id.company_id',
    )
