{
    'name': 'Competency Assessment & Management',
    'version': '19.0.0.1.0',
    'category': 'Human Resources',
    'summary': 'Discipline-based competency frameworks with self-assessment, lead review, and evidence tracking.',
    'description': """
        Competency Assessment & Management
        ==================================
        
        Define discipline-based competency frameworks with configurable
        proficiency levels and criteria. Employees perform self-assessments,
        upload evidence, and receive confirmation from discipline leads.
        
        Key features:
        * Disciplines → Competencies → Criteria per level
        * Configurable proficiency levels (Supervised, Practitioner, Lead Practitioner, etc.)
        * Active/inactive competency toggling
        * Versioned framework snapshots at assessment time
        * Self-assessment wizard with evidence uploads
        * Dual-confirmation workflow (Employee + Discipline Lead)
        * Assessment register (latest + historical views)
        * Role-based access (Admin, Discipline Lead, Employee)
    """,
    'author': 'Damuza Consulting',
    'website': 'https://bowtie-modeler.com',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        # Security
        'security/competency_security.xml',
        'security/ir.model.access.csv',
        # Data (demo levels)
        'data/competency_demo_data.xml',
        # Views
        'views/competency_discipline_views.xml',
        'views/competency_level_views.xml',
        'views/competency_competency_views.xml',
        'views/competency_assessment_views.xml',
        'views/competency_menus.xml',
        # Wizards
        'wizards/self_assessment_wizard_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
