# -*- coding: utf-8 -*-
{
    'name': 'Supplier Management',
    'version': '19.0.0.1.0',
    'category': 'Supply Chain/Supplier',
    'sequence': 36,
    'summary': 'Manage supplier contracts, recurring orders, and direct debit',
    'website': 'https://www.odoo.com',
    'depends': ['purchase', 'account', 'contacts'],
    'data': [
        'security/supplier_security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/res_partner_views.xml',
        'views/supplier_contract_views.xml',
        'views/supplier_contract_line_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'author': 'Supplier Management',
    'license': 'LGPL-3',
}
