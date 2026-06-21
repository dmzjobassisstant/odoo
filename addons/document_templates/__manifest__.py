{
    'name': 'Document Templates',
    'version': '19.0.0.1.0',
    'category': 'Documents',
    'summary': 'Enhanced PDF document templates for invoices, payslips, and more',
    'description': """
Document Templates Module
=========================
- Enhanced invoice PDF with service codes, tax summary, payment terms, bank details
- Document Template model (document.template) for customizing headers, footers, CSS
- Professional formatting for invoices, payslips, and contracts
- Integration with account, hr_payroll_custom, and contract_management
    """,
    'author': 'Nous Research',
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
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
