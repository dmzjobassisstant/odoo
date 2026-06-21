from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ClientReturn(models.Model):
    _name = 'client.return'
    _description = 'Client Return / RMA'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(
        string='Return Reference',
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
        string='Original Sale Order',
        tracking=True,
    )
    invoice_id = fields.Many2one(
        'account.move',
        string='Original Invoice',
        domain=[('move_type', 'in', ('out_invoice', 'out_refund'))],
        tracking=True,
    )
    return_reason = fields.Selection(
        [
            ('defective', 'Defective'),
            ('wrong_item', 'Wrong Item'),
            ('not_needed', 'Not Needed'),
            ('damaged', 'Damaged'),
            ('other', 'Other'),
        ],
        string='Return Reason',
        default='defective',
        required=True,
        tracking=True,
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('approved', 'Approved'),
            ('received', 'Received'),
            ('refunded', 'Refunded'),
            ('rejected', 'Rejected'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
    )
    return_line_ids = fields.One2many(
        'client.return.line',
        'return_id',
        string='Return Lines',
        copy=True,
    )
    refund_invoice_id = fields.Many2one(
        'account.move',
        string='Credit Note',
        readonly=True,
        copy=False,
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('client.return') or _('New')
        return super().create(vals_list)

    def action_approve(self):
        for rma in self:
            if rma.state != 'draft':
                raise UserError(_('Only draft returns can be approved.'))
            if not rma.return_line_ids:
                raise UserError(_('You must add at least one return line before approving.'))
            rma.state = 'approved'
        return True

    def action_receive(self):
        for rma in self:
            if rma.state != 'approved':
                raise UserError(_('Only approved returns can be marked as received.'))
            rma.state = 'received'
            for line in rma.return_line_ids:
                if line.state == 'pending':
                    line.state = 'received'
        return True

    def action_inspect(self):
        for rma in self:
            if rma.state != 'received':
                raise UserError(_('Only received returns can be inspected.'))
            for line in rma.return_line_ids:
                if line.state == 'received':
                    line.state = 'inspected'
        return True

    def action_refund(self):
        for rma in self:
            if rma.state != 'received':
                raise UserError(_('You can only refund received returns.'))
            if not rma.return_line_ids.filtered(lambda l: l.state == 'inspected'):
                raise UserError(_('At least one line must be inspected before refunding.'))

            refund_lines = []
            for line in rma.return_line_ids.filtered(lambda l: l.state == 'inspected'):
                refund_line_vals = {
                    'product_id': line.product_id.id,
                    'name': line.reason or line.product_id.display_name,
                    'quantity': line.quantity,
                    'price_unit': 0.0,
                }
                if rma.invoice_id:
                    invoice_lines = rma.invoice_id.invoice_line_ids.filtered(
                        lambda l: l.product_id == line.product_id
                    )
                    if invoice_lines:
                        refund_line_vals['price_unit'] = invoice_lines[0].price_unit
                refund_lines.append((0, 0, refund_line_vals))

            if rma.invoice_id and rma.invoice_id.state == 'posted':
                # Create credit note from invoice
                move_reversal = self.env['account.move.reversal'].with_context(
                    active_model='account.move',
                    active_ids=rma.invoice_id.ids,
                ).create({
                    'date': fields.Date.context_today(self),
                    'reason': _('Return: %s - %s') % (rma.name, dict(self._fields['return_reason'].selection).get(rma.return_reason, '')),
                    'journal_id': rma.invoice_id.journal_id.id,
                })
                reversal = move_reversal.refund_moves()
                refund_invoice = self.env['account.move'].browse(reversal['res_id'])
                rma.refund_invoice_id = refund_invoice.id
            else:
                # Create standalone credit note
                invoice_vals = {
                    'move_type': 'out_refund',
                    'partner_id': rma.partner_id.id,
                    'invoice_date': fields.Date.context_today(self),
                    'invoice_line_ids': refund_lines,
                }
                refund_invoice = self.env['account.move'].create(invoice_vals)
                rma.refund_invoice_id = refund_invoice.id

            rma.state = 'refunded'
            for line in rma.return_line_ids.filtered(lambda l: l.state == 'inspected'):
                line.state = 'refunded'
        return True

    def action_reject(self):
        for rma in self:
            if rma.state not in ('draft', 'approved'):
                raise UserError(_('Only draft or approved returns can be rejected.'))
            rma.state = 'rejected'
            for line in rma.return_line_ids:
                line.state = 'rejected'
        return True

    def action_cancel(self):
        for rma in self:
            if rma.state in ('refunded', 'cancelled'):
                raise UserError(_('Cannot cancel a refunded or already cancelled return.'))
            rma.state = 'cancelled'
        return True

    def action_set_draft(self):
        for rma in self:
            if rma.state not in ('rejected', 'cancelled'):
                raise UserError(_('Only rejected or cancelled returns can be reset to draft.'))
            rma.state = 'draft'
            for line in rma.return_line_ids:
                line.state = 'pending'
        return True

    def action_view_refund(self):
        self.ensure_one()
        if not self.refund_invoice_id:
            raise UserError(_('No credit note generated yet.'))
        return {
            'type': 'ir.actions.act_window',
            'name': _('Credit Note'),
            'res_model': 'account.move',
            'res_id': self.refund_invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
