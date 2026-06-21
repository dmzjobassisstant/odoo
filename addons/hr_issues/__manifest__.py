{
    'name': 'HR Issues',
    'version': '19.0.0.1.0',
    'category': 'Human Resources',
    'summary': 'HR Case Management - Grievances, Disputes, Tickets',
    'description': """
HR Issues Management
====================
Track and manage HR cases including grievances, disputes, harassment complaints,
and general HR tickets.

Features:
- Case lifecycle: draft → open → investigating → resolved → closed
- Confidential issues with restricted visibility
- Internal notes with visibility control
- Assignment and tracking
    """,
    'author': 'Your Company',
    'website': 'https://www.example.com',
    'depends': ['hr', 'mail'],
    'data': [
        'security/hr_issues_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/hr_issue_views.xml',
        'views/hr_issue_note_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
