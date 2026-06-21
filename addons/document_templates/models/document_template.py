from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DocumentTemplate(models.Model):
    _name = 'document.template'
    _description = 'Document Template'
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True,
    )
    model = fields.Selection(
        [
            ('sale.order', 'Sale Order'),
            ('account.move', 'Invoice / Account Move'),
            ('hr.payslip', 'Payslip'),
            ('client.contract', 'Client Contract'),
        ],
        string='Applies To Model',
        required=True,
        tracking=True,
    )
    template_type = fields.Selection(
        [
            ('invoice', 'Invoice'),
            ('payslip', 'Payslip'),
            ('contract', 'Contract'),
            ('report', 'General Report'),
        ],
        string='Template Type',
        required=True,
        tracking=True,
    )
    header_html = fields.Text(
        string='Custom Header HTML',
        help='HTML content for the document header. '
             'Use variables like {company_name}, {company_address}, '
             '{document_date}, {document_number}.',
    )
    footer_html = fields.Text(
        string='Custom Footer HTML',
        help='HTML content for the document footer. '
             'Use variables like {company_name}, {bank_details}, '
             '{payment_terms}, {page_number}.',
    )
    css_override = fields.Text(
        string='CSS Override',
        help='Custom CSS styles to apply to the document. '
             'Will be embedded in the PDF output.',
    )
    is_default = fields.Boolean(
        string='Default Template',
        default=False,
        help='If checked, this template will be used as the default '
             'for its model and template type.',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
        tracking=True,
    )
    active = fields.Boolean(
        string='Active',
        default=True,
        tracking=True,
    )

    _unique_default_per_type = models.Constraint(
        'UNIQUE(model, template_type, company_id, is_default)',
        message='Only one default template can exist per model, '
                'template type, and company.',
    )

    @api.constrains('is_default')
    def _check_only_one_default(self):
        for rec in self:
            if rec.is_default:
                domain = [
                    ('model', '=', rec.model),
                    ('template_type', '=', rec.template_type),
                    ('company_id', '=', rec.company_id.id),
                    ('is_default', '=', True),
                    ('id', '!=', rec.id),
                ]
                existing = self.search_count(domain)
                if existing:
                    raise ValidationError(_(
                        'A default template already exists for this '
                        'model/template type/company combination.'
                    ))

    @api.onchange('model')
    def _onchange_model(self):
        """Suggest template_type based on model."""
        if self.model:
            model_to_type = {
                'account.move': 'invoice',
                'sale.order': 'report',
                'hr.payslip': 'payslip',
                'client.contract': 'contract',
            }
            self.template_type = model_to_type.get(self.model, 'report')
