{
    'name': 'Scheduled Reminders',
    'version': '19.0.0.1.0',
    'category': 'Productivity',
    'summary': 'Schedule reminders based on record state or date triggers',
    'description': """
Scheduled Reminders Module
==========================

Automatically send reminders based on record state or date triggers.
Supports timesheet submissions, training due dates, payslip approvals,
and offboarding checklists.

Features:
- State-based triggers (e.g., remind when timesheet is in draft)
- Date-based triggers (e.g., remind N days before a due date)
- Flexible recipient resolution (per-record or per-group)
- Activity-based notification engine
- Deduplication via reminder.log
    """,
    'author': 'Nous Research',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/reminder_cron.xml',
        'data/reminder_data.xml',
        'views/reminder_rule_views.xml',
        'views/reminder_log_views.xml',
        'views/menu_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
