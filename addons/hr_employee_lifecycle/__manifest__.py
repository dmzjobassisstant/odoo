{
    'name': 'HR Employee Lifecycle',
    'version': '19.0.0.1.0',
    'category': 'Human Resources',
    'summary': 'Manage the full employee lifecycle from recruitment to offboarding',
    'description': """
HR Employee Lifecycle
=====================
Full employee journey management:
- Recruitment → Contract → Probation → Active Employment
- Leave Management
- Offboarding (resignation, retirement, redundancy with settlement calculations)

Features:
- Extended employee records with employment status tracking
- Contract management with type, notice periods, and redundancy calculations
- Offboarding process with task checklists
- Settlement calculation support for redundancy
""",
    'author': 'Nous Research',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['hr', 'hr_holidays'],
    'data': [
        'security/hr_employee_lifecycle_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_employee_lifecycle_rules.xml',
        'views/hr_employee_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_offboarding_views.xml',
        'views/hr_employee_lifecycle_menus.xml',
        'data/hr_offboarding_task_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
}
