{
    'name': 'Menu Consolidation',
    'version': '19.0.0.1.0',
    'category': 'Hidden',
    'summary': 'Consolidates 26 top-level menus into 7 grouped menus (1-5 apps each)',
    'description': """
Groups the app drawer into logical parent menus:

- HR & Payroll (5): Employees, Recruitment, Time Off, Payroll, HR Issues
- Finance (3): Invoicing, Sales, Expenses
- Operations (3): Timesheets, Project, To-do
- Supply Chain (3): Purchase, Supplier Management, Contract Management
- Strategy (3): Board Reports, Competencies, Dashboards
- Tools (4): Calendar, Contacts, Discuss, Document Layouts
- System (3): Settings, Link Tracker, Website

Hides "Apps" and "Tests" from the drawer.
    """,
    'author': 'Damuza Consulting',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['base'],
    'data': [
        'data/menu_groups.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
