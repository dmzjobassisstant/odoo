from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    contract_ids = fields.One2many(
        'client.contract',
        'partner_id',
        string='Contracts',
    )
    contract_count = fields.Integer(
        string='Contract Count',
        compute='_compute_contract_count',
    )
    return_ids = fields.One2many(
        'client.return',
        'partner_id',
        string='Returns',
    )
    return_count = fields.Integer(
        string='Return Count',
        compute='_compute_return_count',
    )

    def _compute_contract_count(self):
        for partner in self:
            partner.contract_count = self.env['client.contract'].search_count([
                ('partner_id', '=', partner.id),
            ])

    def _compute_return_count(self):
        for partner in self:
            partner.return_count = self.env['client.return'].search_count([
                ('partner_id', '=', partner.id),
            ])

    def action_view_contracts(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contracts',
            'res_model': 'client.contract',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }

    def action_view_returns(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Returns',
            'res_model': 'client.return',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }
