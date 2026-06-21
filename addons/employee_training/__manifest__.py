{
    'name': 'Employee Training',
    'version': '19.0.0.1.0',
    'category': 'Human Resources',
    'summary': 'Manage employee training plans, courses, assignments, and SCORM-compatible e-learning',
    'description': """
Employee Training Module
========================

Features:
- Training Plans organized by category (onboarding, compliance, technical, soft skills, safety)
- Courses with multiple types: SCORM, video, document, quiz
- SCORM 1.2 compatible e-learning content with runtime API
- Assignments with progress tracking and due dates
- Completion certificates
- Integration with employee onboarding/offboarding
    """,
    'author': 'Nous Research',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/training_cron.xml',
        'views/training_plan_views.xml',
        'views/training_course_views.xml',
        'views/training_assignment_views.xml',
        'views/training_completion_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
