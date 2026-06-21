{
    'name': 'Timesheet Management',
    'version': '19.0.0.3.0',
    'category': 'Human Resources',
    'summary': 'Weekly timesheet submission with matrix entry grid, submission workflow, and Excel reporting',
    'description': """
Timesheet Management Module
===========================

A comprehensive weekly timesheet module for Odoo 19 that provides:

* **On-demand task adding** — select tasks for the week; each task auto-creates
  7 day slots (Mon-Sun). Copy task list from previous week.
* **Workflow**: Draft → Submitted (locked) → Completed (billed)
  - Submitted timesheets are read-only for the user
  - Administrators can unlock, mark completed, or return for billing disputes
* **Excel reports** — per-project reports with cover page, per-employee tabs,
  and summary sheet with invoiced hours.
""",
    'author': 'Damuza Consulting',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['base', 'hr', 'hr_timesheet', 'project', 'mail', 'web'],
    'data': [
        'security/timesheet_security.xml',
        'security/ir.model.access.csv',
        'views/timesheet_week_views.xml',
        'views/timesheet_entry_views.xml',
        'views/timesheet_menus.xml',
        'wizards/timesheet_report_views.xml',
        'wizards/timesheet_add_tasks_views.xml',
    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
