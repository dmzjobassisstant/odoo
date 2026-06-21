import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class ClientContract(models.Model):
    _name = 'client.contract'
    _description = 'Client Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(
        string='Contract Reference',
        default=lambda self: _('New'),
        copy=False,
        readonly=True,
        tracking=True,
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        tracking=True,
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Originating Sale Order',
        tracking=True,
    )
    contract_type = fields.Selection(
        [
            ('service', 'Service'),
            ('subscription', 'Subscription'),
            ('retainer', 'Retainer'),
            ('product_sale', 'Product Sale'),
        ],
        string='Contract Type',
        default='service',
        required=True,
        tracking=True,
    )
    start_date = fields.Date(
        string='Start Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )
    end_date = fields.Date(
        string='End Date',
        tracking=True,
    )
    recurring_interval = fields.Selection(
        [
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('annually', 'Annually'),
            ('one_time', 'One Time'),
        ],
        string='Recurring Interval',
        default='monthly',
        tracking=True,
    )
    recurring_amount = fields.Float(
        string='Recurring Amount',
        tracking=True,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('suspended', 'Suspended'),
            ('expired', 'Expired'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
    )
    contract_line_ids = fields.One2many(
        'client.contract.line',
        'contract_id',
        string='Contract Lines',
        copy=True,
    )
    auto_invoice = fields.Boolean(
        string='Auto Generate Invoices',
        default=False,
        tracking=True,
    )
    next_invoice_date = fields.Date(
        string='Next Invoice Date',
        tracking=True,
    )
    invoice_ids = fields.One2many(
        'account.move',
        'contract_id',
        string='Linked Invoices',
        copy=False,
    )
    invoice_count = fields.Integer(
        string='Invoice Count',
        compute='_compute_invoice_count',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
    )
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
    )

    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for contract in self:
            contract.invoice_count = len(contract.invoice_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('client.contract') or _('New')
        return super().create(vals_list)

    def action_activate(self):
        for contract in self:
            if contract.state != 'draft':
                raise UserError(_('Only draft contracts can be activated.'))
            if not contract.contract_line_ids:
                raise UserError(_('You must add at least one contract line before activating.'))
            contract.state = 'active'
            if contract.auto_invoice and contract.recurring_interval != 'one_time':
                contract._compute_next_invoice_date()
        return True

    def action_suspend(self):
        for contract in self:
            if contract.state != 'active':
                raise UserError(_('Only active contracts can be suspended.'))
            contract.state = 'suspended'
        return True

    def action_resume(self):
        for contract in self:
            if contract.state != 'suspended':
                raise UserError(_('Only suspended contracts can be resumed.'))
            contract.state = 'active'
        return True

    def action_cancel(self):
        for contract in self:
            if contract.state in ('expired', 'cancelled'):
                raise UserError(_('Contract is already cancelled or expired.'))
            contract.state = 'cancelled'
        return True

    def action_set_draft(self):
        for contract in self:
            if contract.state != 'cancelled':
                raise UserError(_('Only cancelled contracts can be reset to draft.'))
            contract.state = 'draft'
        return True

    def _compute_next_invoice_date(self):
        self.ensure_one()
        if not self.next_invoice_date or self.next_invoice_date <= fields.Date.context_today(self):
            self.next_invoice_date = fields.Date.context_today(self)
        else:
            return
        intervals = {
            'weekly': relativedelta(weeks=1),
            'monthly': relativedelta(months=1),
            'quarterly': relativedelta(months=3),
            'annually': relativedelta(years=1),
        }
        if self.recurring_interval in intervals:
            self.next_invoice_date += intervals[self.recurring_interval]

    def action_generate_invoice(self):
        self.ensure_one()
        if self.state != 'active':
            raise UserError(_('You can only generate invoices for active contracts.'))
        if not self.contract_line_ids:
            raise UserError(_('Contract has no lines to invoice.'))

        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_date': fields.Date.context_today(self),
            'contract_id': self.id,
            'invoice_line_ids': [],
        }
        for line in self.contract_line_ids:
            invoice_line_vals = {
                'product_id': line.product_id.id,
                'name': line.description or line.product_id.display_name,
                'quantity': line.quantity,
                'price_unit': line.unit_price,
                'tax_ids': [(6, 0, [line.tax_id.id])] if line.tax_id else [],
            }
            invoice_vals['invoice_line_ids'].append((0, 0, invoice_line_vals))

        invoice = self.env['account.move'].create(invoice_vals)
        if self.auto_invoice:
            self._compute_next_invoice_date()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Generated Invoice'),
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_view_invoices(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Linked Invoices'),
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'domain': [('contract_id', '=', self.id)],
            'target': 'current',
        }

    def action_return_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Return'),
            'res_model': 'client.return',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_sale_order_id': self.sale_order_id.id,
            },
        }

    def _cron_check_expired_contracts(self):
        """Cron job to expire contracts past their end date."""
        today = fields.Date.context_today(self)
        expired = self.search([
            ('state', '=', 'active'),
            ('end_date', '!=', False),
            ('end_date', '<', today),
        ])
        expired.write({'state': 'expired'})

    def _cron_generate_recurring_invoices(self):
        """Cron job to auto-generate invoices for contracts due today."""
        today = fields.Date.context_today(self)
        contracts = self.search([
            ('state', '=', 'active'),
            ('auto_invoice', '=', True),
            ('recurring_interval', '!=', 'one_time'),
            ('next_invoice_date', '<=', today),
        ])
        for contract in contracts:
            try:
                contract.action_generate_invoice()
            except Exception as e:
                _logger.exception('Failed to generate recurring invoice for contract %s: %s', contract.name, e)
