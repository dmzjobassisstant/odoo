{
    'name': 'Board Reporting',
    'version': '19.0.0.1.0',
    'category': 'Human Resources',
    'summary': 'Configurable business metrics/KPIs for board presentations',
    'description': """
Board Reporting Module
======================

Provides configurable business metrics and KPI tracking for board-level reporting.

Features:
- Define custom metrics/KPIs with calculation formulas
- Generate board reports for any period
- Auto-calculate all active metrics when generating reports
- Trend tracking (up/down/stable) against previous periods
- Dashboard-style report view with metric tiles

Built-in metrics:
- Employee Utilisation Rate
- Headcount
- Attrition/Turnover Rate
- Absenteeism Rate
- Billable Hours
- Revenue per Employee
- Average Resolution Time
- Open Issues
    """,
    'author': 'Nous Research',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['hr', 'timesheet_management', 'hr_employee_lifecycle', 'hr_payroll_custom'],
    'data': [
        'security/board_reporting_security.xml',
        'security/ir.model.access.csv',
        'data/board_metric_data.xml',
        'views/board_metric_views.xml',
        'views/board_metric_value_views.xml',
        'views/board_report_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
