# -*- coding: utf-8 -*-
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SupplierContract(models.Model):
    _name = 'supplier.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Supplier Contract'
    _order = 'id desc'
    _rec_names_search = ['name', 'partner_id']

    name = fields.Char(string='Contract Reference', required=True, copy=False,
                       default=lambda self: _('New'))
    partner_id = fields.Many2one(
        'res.partner', string='Supplier', required=True,
        domain="[('supplier_rank','>', 0)]",
        tracking=True,
    )
    contract_type = fields.Selection([
        ('service', 'Service'),
        ('goods', 'Goods'),
        ('lease', 'Lease'),
        ('maintenance', 'Maintenance'),
    ], string='Contract Type', required=True, default='service')
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    recurring_interval = fields.Selection([
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    ], string='Recurring Interval', default='monthly')
    recurring_amount = fields.Float(string='Recurring Amount')
    payment_method = fields.Selection([
        ('direct_debit', 'Direct Debit'),
        ('bank_transfer', 'Bank Transfer'),
        ('standing_order', 'Standing Order'),
    ], string='Payment Method')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True, required=True)
    contract_line_ids = fields.One2many(
        'supplier.contract.line', 'contract_id',
        string='Contract Lines', copy=True,
    )
    auto_generate_orders = fields.Boolean(
        string='Auto-Generate Purchase Orders',
        default=False,
        help='Automatically create purchase orders based on recurring schedule',
    )
    next_order_date = fields.Date(
        string='Next Order Date',
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        related='company_id.currency_id',
    )
    active = fields.Boolean(default=True)

    @api.depends('name', 'partner_id.display_name')
    def _compute_display_name(self):
        for rec in self:
            if rec.partner_id:
                rec.display_name = f"{rec.name} - {rec.partner_id.display_name}"
            else:
                rec.display_name = rec.name or ''

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('supplier.contract') or _('New')
        return super().create(vals_list)

    def _compute_next_order_date(self):
        """Compute the next order date based on interval"""
        self.ensure_one()
        interval_map = {
            'weekly': relativedelta(weeks=1),
            'monthly': relativedelta(months=1),
            'quarterly': relativedelta(months=3),
            'annually': relativedelta(years=1),
        }
        delta = interval_map.get(self.recurring_interval, relativedelta(months=1))
        base_date = self.next_order_date or self.start_date or date.today()
        return base_date + delta

    def action_activate(self):
        for contract in self:
            if contract.state != 'draft':
                raise UserError(_('Only draft contracts can be activated.'))
            if not contract.start_date:
                raise UserError(_('Start date is required to activate the contract.'))
            contract.write({
                'state': 'active',
                'next_order_date': contract.start_date,
            })
        return True

    def action_draft(self):
        for contract in self:
            if contract.state not in ('cancelled',):
                raise UserError(_('Only cancelled contracts can be reset to draft.'))
            contract.state = 'draft'
        return True

    def action_cancel(self):
        for contract in self:
            if contract.state in ('expired',):
                raise UserError(_('Expired contracts cannot be cancelled.'))
            contract.state = 'cancelled'

    def action_expire(self):
        for contract in self:
            if contract.state != 'active':
                raise UserError(_('Only active contracts can be marked as expired.'))
            contract.state = 'expired'
            contract.next_order_date = False

    def cron_generate_purchase_orders(self):
        """Cron job: Auto-generate purchase orders for active recurring contracts"""
        today = date.today()
        contracts = self.search([
            ('state', '=', 'active'),
            ('auto_generate_orders', '=', True),
            ('next_order_date', '<=', today),
        ])
        _logger.info('Auto-generating purchase orders for %d contracts', len(contracts))
        for contract in contracts:
            try:
                contract._generate_purchase_order()
            except Exception as e:
                _logger.error('Failed to generate PO for contract %s: %s', contract.name, str(e))

    def _generate_purchase_order(self):
        """Generate a purchase order from this contract"""
        self.ensure_one()
        if not self.contract_line_ids:
            raise UserError(_('Contract %s has no lines to generate an order.') % self.name)

        po_vals = {
            'partner_id': self.partner_id.id,
            'origin': self.name,
            'date_order': fields.Datetime.now(),
            'company_id': self.company_id.id,
            'order_line': [],
        }
        for line in self.contract_line_ids:
            po_line_vals = {
                'product_id': line.product_id.id,
                'name': line.description or line.product_id.display_name,
                'product_qty': line.quantity,
                'price_unit': line.unit_price,
                'taxes_id': [(6, 0, line.tax_id.ids)] if line.tax_id else [],
                'date_planned': fields.Datetime.now(),
            }
            po_vals['order_line'].append((0, 0, po_line_vals))

        po = self.env['purchase.order'].create(po_vals)
        self.message_post(
            body=_('Purchase Order %s generated from contract.') % po.name,
        )
        # Advance next_order_date
        self.next_order_date = self._compute_next_order_date()
        return po
