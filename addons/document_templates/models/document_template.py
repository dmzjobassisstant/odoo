from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DocumentTemplate(models.Model):
    _name = 'document.template'
    _description = 'Document Layout'
    _order = 'template_type, model, name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # ---- Identity ----
    name = fields.Char(
        string='Layout Name',
        required=True,
        tracking=True,
        help='Descriptive name for this layout (e.g. "Standard Invoice v2").',
    )
    model = fields.Selection([
        ('account.move', 'Invoice / Account Move'),
        ('hr.payslip', 'Payslip'),
        ('client.contract', 'Client Contract'),
        ('supplier.contract', 'Supplier Contract'),
        ('sale.order', 'Sale Order / Quotation'),
    ], string='Applies To', required=True, tracking=True,
       help='Which Odoo model this layout is assigned to.')
    template_type = fields.Selection([
        ('invoice', 'Invoice'),
        ('payslip', 'Payslip'),
        ('contract', 'Contract'),
        ('report', 'General Report'),
    ], string='Document Type', required=True, tracking=True)
    is_default = fields.Boolean(
        string='Default Layout',
        default=False,
        help='When checked, this layout is used automatically when printing '
             'from the assigned module. Only one default per model/type/company.',
    )
    active = fields.Boolean(default=True, tracking=True)
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
        required=True, tracking=True,
    )

    # ---- Branding ----
    logo = fields.Binary(
        string='Company Logo',
        help='Upload a logo image (PNG or JPEG). Displayed in the header of every PDF.',
        attachment=True,
    )
    logo_filename = fields.Char(string='Logo Filename')
    primary_color = fields.Char(
        string='Primary Color',
        default='#261e58',
        help='Main brand color — used for headings, table headers, borders, and accents.',
    )
    secondary_color = fields.Char(
        string='Secondary Color',
        default='#f0eef7',
        help='Subtle brand color — used for table header backgrounds, card headers, and light accents.',
    )
    font_family = fields.Selection([
        ('helvetica', 'Helvetica (clean, modern)'),
        ('times', 'Times New Roman (serif, formal)'),
        ('courier', 'Courier (monospace)'),
    ], string='Font', default='helvetica',
       help='Base font for the PDF document.')

    # ---- Layout Overrides ----
    header_html = fields.Text(
        string='Custom Header HTML',
        help='Raw HTML inserted at the top of every PDF. '
             'Use variables like {company_name}, {document_number}, {document_date}. '
             'Leave blank to use the standard header with logo and company details.',
    )
    footer_html = fields.Text(
        string='Custom Footer HTML',
        help='Raw HTML inserted at the bottom of every PDF. '
             'Leave blank to use the standard footer.',
    )
    css_override = fields.Text(
        string='Custom CSS',
        help='Additional CSS rules injected into the PDF. '
             'The primary/secondary colors are already applied automatically — '
             'use this for fine-tuning specific elements.',
    )

    # ---- Smart defaults ----
    @api.onchange('model')
    def _onchange_model(self):
        if self.model:
            self.template_type = {
                'account.move': 'invoice',
                'hr.payslip': 'payslip',
                'client.contract': 'contract',
                'supplier.contract': 'contract',
                'sale.order': 'report',
            }.get(self.model, 'report')

    @api.constrains('is_default')
    def _check_only_one_default(self):
        for rec in self:
            if rec.is_default:
                existing = self.search_count([
                    ('model', '=', rec.model),
                    ('template_type', '=', rec.template_type),
                    ('company_id', '=', rec.company_id.id),
                    ('is_default', '=', True),
                    ('active', '=', True),
                    ('id', '!=', rec.id),
                ])
                if existing:
                    raise ValidationError(_(
                        'A default layout already exists for this model/type/company.'
                    ))

    # ---- Template stub constraint (Odoo 19 style) ----
