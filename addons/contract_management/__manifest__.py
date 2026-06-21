{
    'name': 'Client Contract & Sales Management',
    'version': '19.0.0.1.0',
    'category': 'Sales/Contract',
    'summary': 'Manage client contracts, recurring billing, and returns/RMA',
    'description': """
Client Contract & Sales Management Module
=========================================
- Client service/sales contracts with recurring billing
- Contract line items with products and pricing
- Returns/RMA management with refund workflow
- Auto-generate invoices for active recurring contracts
- Partner extension with contracts and returns tabs
    """,
    'author': 'Custom',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['sale_management', 'account', 'product'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/client_contract_views.xml',
        'views/client_return_views.xml',
        'views/res_partner_views.xml',
        'data/menu_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
