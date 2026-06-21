{
    'name': 'Document Layouts',
    'version': '19.0.0.2.0',
    'category': 'Documents',
    'summary': 'Define document layouts with branding — logo, colors, fonts — auto-applied when printing',
    'description': """
Document Layouts
===============

A standalone application for defining and managing document layouts.

* **Logo & Branding** — upload your company logo, set primary/secondary colors, choose fonts
* **Auto-assignment** — each layout is assigned to a module (Invoicing, Payroll, Contracts);
  the "Default" flag makes it automatically used when printing
* **Live preview** — CSS and header/footer overrides take effect immediately
* **Modules supported**: account.move (invoices), hr.payslip (payslips),
  client.contract, supplier.contract, sale.order

No separate app-per-module configuration needed. Set the layout once, print anywhere.
    """,
    'author': 'Damuza Consulting',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['account', 'hr_payroll_custom'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_template_views.xml',
        'views/menu_views.xml',
        'reports/report_invoice_enhanced_action.xml',
        'reports/report_invoice_enhanced_template.xml',
        'reports/report_payslip_enhanced_action.xml',
        'reports/report_payslip_enhanced_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
