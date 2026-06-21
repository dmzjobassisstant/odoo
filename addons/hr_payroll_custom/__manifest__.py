{
    'name': 'HR Payroll Custom',
    'version': '19.0.0.1.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Manage employee payslips, salary rules, and payroll processing',
    'description': """
HR Payroll Custom Module
========================
- Generate payslips from timesheet data
- Configurable salary rules (earnings and deductions)
- Payslip workflow: Draft → Confirmed → Paid
- PDF payslip reports
- Integration with Timesheet Management and Employee Lifecycle
    """,
    'author': 'Nous Research',
    'website': 'https://oodoo.bowtie-modeler.com',
    'depends': ['hr', 'hr_employee_lifecycle', 'timesheet_management'],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'data/hr_salary_rule_data.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_payslip_generate_wizard_views.xml',
        'views/menu_views.xml',
        'reports/hr_payslip_report.xml',
        'reports/hr_payslip_report_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
