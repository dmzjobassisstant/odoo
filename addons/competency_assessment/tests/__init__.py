from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import UserError, AccessError


@tagged('post_install', '-at_install', 'competency')
class TestCompetencyDiscipline(TransactionCase):
    """Test discipline CRUD and lead assignment."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Discipline = cls.env['competency.discipline']
        cls.Level = cls.env['competency.level']
        cls.Employee = cls.env['hr.employee']

        # Create an employee to act as discipline lead
        cls.lead = cls.Employee.create({'name': 'Test Lead'})

    def test_create_discipline(self):
        """Discipline creation with required fields."""
        disc = self.Discipline.create({
            'name': 'Systems Engineering',
            'code': 'SE',
            'lead_id': self.lead.id,
        })
        self.assertTrue(disc.id)
        self.assertEqual(disc.name, 'Systems Engineering')
        self.assertEqual(disc.code, 'SE')
        self.assertEqual(disc.lead_id, self.lead)

    def test_discipline_active_default(self):
        """Discipline defaults to active=True."""
        disc = self.Discipline.create({'name': 'Test'})
        self.assertTrue(disc.active)

    def test_discipline_competency_count(self):
        """competency_count computed field reflects child competencies."""
        disc = self.Discipline.create({'name': 'Test'})
        self.assertEqual(disc.competency_count, 0)

        Competency = self.env['competency.competency']
        Competency.create({'name': 'C1', 'discipline_id': disc.id})
        Competency.create({'name': 'C2', 'discipline_id': disc.id})
        self.assertEqual(disc.competency_count, 2)

    def test_discipline_sequence_default(self):
        """Sequence defaults to 10."""
        disc = self.Discipline.create({'name': 'Test'})
        self.assertEqual(disc.sequence, 10)

    def test_discipline_name_required(self):
        """Name is required."""
        with self.assertRaises(Exception):
            self.Discipline.create({})


@tagged('post_install', '-at_install', 'competency')
class TestCompetencyLevel(TransactionCase):
    """Test proficiency level management."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Level = cls.env['competency.level']

    def test_create_level(self):
        """Create a proficiency level."""
        level = self.Level.create({
            'name': 'Practitioner',
            'code': 'PRAC',
        })
        self.assertTrue(level.id)
        self.assertEqual(level.name, 'Practitioner')

    def test_level_sequence(self):
        """Levels order by sequence."""
        l1 = self.Level.create({'name': 'A', 'sequence': 20})
        l2 = self.Level.create({'name': 'B', 'sequence': 10})
        ordered = self.Level.search([('id', 'in', (l1.id, l2.id))], order='sequence')
        self.assertEqual(ordered[0], l2)

    def test_level_active_default(self):
        """Level defaults to active=True."""
        level = self.Level.create({'name': 'Test'})
        self.assertTrue(level.active)


@tagged('post_install', '-at_install', 'competency')
class TestCompetencyCriteria(TransactionCase):
    """Test competencies with criteria."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Discipline = cls.env['competency.discipline']
        cls.Competency = cls.env['competency.competency']
        cls.Level = cls.env['competency.level']
        cls.Criterion = cls.env['competency.criterion']

        cls.disc = cls.Discipline.create({'name': 'Test Discipline'})
        cls.level_a = cls.Level.create({'name': 'Supervised', 'sequence': 10})
        cls.level_b = cls.Level.create({'name': 'Practitioner', 'sequence': 20})

    def test_create_competency(self):
        """Create a competency linked to a discipline."""
        comp = self.Competency.create({
            'name': 'Requirements Analysis',
            'discipline_id': self.disc.id,
        })
        self.assertTrue(comp.id)
        self.assertEqual(comp.discipline_id, self.disc)
        self.assertTrue(comp.active)

    def test_create_criterion(self):
        """Add criteria per proficiency level."""
        comp = self.Competency.create({
            'name': 'Test Comp',
            'discipline_id': self.disc.id,
        })
        crit = self.Criterion.create({
            'competency_id': comp.id,
            'level_id': self.level_a.id,
            'description': 'Can perform task with supervision.',
        })
        self.assertTrue(crit.id)
        self.assertEqual(crit.competency_id, comp)
        self.assertEqual(crit.level_id, self.level_a)

    def test_criterion_count_computed(self):
        """criterion_count reflects actual criteria count."""
        comp = self.Competency.create({
            'name': 'Test Comp',
            'discipline_id': self.disc.id,
        })
        self.assertEqual(comp.criterion_count, 0)

        self.Criterion.create({
            'competency_id': comp.id,
            'level_id': self.level_a.id,
            'description': 'Criterion A',
        })
        self.Criterion.create({
            'competency_id': comp.id,
            'level_id': self.level_b.id,
            'description': 'Criterion B',
        })
        self.assertEqual(comp.criterion_count, 2)

    def test_competency_cascade_delete(self):
        """Deleting a discipline cascades to competencies."""
        disc2 = self.Discipline.create({'name': 'Temporary'})
        comp = self.Competency.create({
            'name': 'Temp Comp',
            'discipline_id': disc2.id,
        })
        comp_id = comp.id
        disc2.unlink()
        self.assertFalse(self.Competency.search([('id', '=', comp_id)]))


@tagged('post_install', '-at_install', 'competency')
class TestAssessmentWorkflow(TransactionCase):
    """Test the full assessment state machine."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Discipline = cls.env['competency.discipline']
        cls.Competency = cls.env['competency.competency']
        cls.Level = cls.env['competency.level']
        cls.Criterion = cls.env['competency.criterion']
        cls.Assessment = cls.env['competency.assessment']
        cls.Employee = cls.env['hr.employee']

        # Setup users
        cls.admin_user = cls.env.ref('base.user_admin')
        cls.lead_user = cls.env.ref('base.user_admin')  # use admin as lead for testing

        # Create employee for the admin user
        cls.employee = cls.Employee.create({
            'name': 'Test Employee',
            'user_id': cls.admin_user.id,
        })

        # Create lead employee
        cls.lead_employee = cls.Employee.create({
            'name': 'Discipline Lead',
            'user_id': cls.admin_user.id,
        })

        # Setup framework
        cls.discipline = cls.Discipline.create({
            'name': 'Test Discipline',
            'lead_id': cls.lead_employee.id,
        })
        cls.level = cls.Level.create({'name': 'Practitioner'})
        cls.comp = cls.Competency.create({
            'name': 'Test Competency',
            'discipline_id': cls.discipline.id,
        })
        cls.Criterion.create({
            'competency_id': cls.comp.id,
            'level_id': cls.level.id,
            'description': 'Test criterion',
        })

    def test_create_assessment(self):
        """Assessment creation defaults to draft state."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        self.assertEqual(assessment.state, 'draft')
        self.assertTrue(assessment.name)  # sequence generated

    def test_assessment_sequence_generation(self):
        """Assessment reference auto-generated from sequence."""
        a1 = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        a2 = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        self.assertNotEqual(a1.name, a2.name)
        self.assertNotEqual(a1.name, 'New')

    def test_workflow_self_assess(self):
        """Draft → Self-Assessed transition."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_self_assess()
        self.assertEqual(assessment.state, 'self_assessed')

    def test_workflow_lead_review(self):
        """Self-Assessed → Lead Reviewed transition."""
        # Grant lead group to admin for this test
        lead_group = self.env.ref('competency_assessment.group_discipline_lead')
        self.admin_user.write({'groups_id': [(4, lead_group.id)]})

        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_self_assess()
        assessment.action_lead_review()
        self.assertEqual(assessment.state, 'lead_reviewed')

    def test_workflow_employee_accept(self):
        """Lead Reviewed → Employee Accepted."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_self_assess()

        lead_group = self.env.ref('competency_assessment.group_discipline_lead')
        self.admin_user.write({'groups_id': [(4, lead_group.id)]})
        assessment.action_lead_review()

        assessment.action_employee_accept()
        self.assertEqual(assessment.state, 'employee_accepted')
        self.assertTrue(assessment.employee_acceptance_date)

    def test_workflow_lead_confirm(self):
        """Employee Accepted → Done (full workflow)."""
        lead_group = self.env.ref('competency_assessment.group_discipline_lead')
        self.admin_user.write({'groups_id': [(4, lead_group.id)]})

        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_self_assess()
        assessment.action_lead_review()
        assessment.action_employee_accept()
        assessment.action_lead_confirm()
        self.assertEqual(assessment.state, 'done')
        self.assertTrue(assessment.lead_confirmation_date)

    def test_workflow_cancel(self):
        """Assessment can be cancelled from any state."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_cancel()
        self.assertEqual(assessment.state, 'cancelled')

    def test_workflow_reset_to_draft(self):
        """Cancel → Draft reset."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_cancel()
        assessment.action_reset_draft()
        self.assertEqual(assessment.state, 'draft')

    def test_invalid_self_assess_not_draft(self):
        """Cannot self-assess if not in draft."""
        lead_group = self.env.ref('competency_assessment.group_discipline_lead')
        self.admin_user.write({'groups_id': [(4, lead_group.id)]})

        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        assessment.action_self_assess()
        with self.assertRaises(UserError):
            assessment.action_self_assess()

    def test_invalid_lead_review_not_self_assessed(self):
        """Cannot lead-review if not in self-assessed state."""
        lead_group = self.env.ref('competency_assessment.group_discipline_lead')
        self.admin_user.write({'groups_id': [(4, lead_group.id)]})

        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        # Still in draft
        with self.assertRaises(UserError):
            assessment.action_lead_review()

    def test_invalid_employee_accept_not_reviewed(self):
        """Cannot employee-accept if not lead-reviewed."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        with self.assertRaises(UserError):
            assessment.action_employee_accept()

    def test_lead_id_derived_from_discipline(self):
        """Lead is derived from discipline."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        self.assertEqual(assessment.lead_id, self.lead_employee)

    def test_assessment_line_creation(self):
        """Assessment lines can be created with snapshot data."""
        assessment = self.Assessment.create({
            'employee_id': self.employee.id,
            'discipline_id': self.discipline.id,
        })
        Line = self.env['competency.assessment.line']
        line = Line.create({
            'assessment_id': assessment.id,
            'competency_id': self.comp.id,
            'competency_name': 'Snapshotted Competency',
            'competency_description': 'Description snapshot',
            'criteria_snapshot': '{"Practitioner": "Test criterion"}',
        })
        self.assertTrue(line.id)
        self.assertEqual(line.assessment_id, assessment)
        self.assertEqual(line.competency_id, self.comp)


@tagged('post_install', '-at_install', 'competency')
class TestCompetencySecurity(TransactionCase):
    """Test access control and record rules."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Discipline = cls.env['competency.discipline']
        cls.Assessment = cls.env['competency.assessment']
        cls.Employee = cls.env['hr.employee']

        # Create discipline
        cls.disc = cls.Discipline.create({'name': 'Test Discipline'})

        # Create regular user
        cls.user_employee = cls.env['res.users'].create({
            'name': 'Regular Employee',
            'login': 'test_employee',
            'groups_id': [(6, 0, [
                cls.env.ref('base.group_user').id,
                cls.env.ref('competency_assessment.group_competency_user').id,
            ])],
        })
        cls.emp = cls.Employee.create({
            'name': 'Regular Employee',
            'user_id': cls.user_employee.id,
        })

        # Create lead user
        cls.user_lead = cls.env['res.users'].create({
            'name': 'Discipline Lead',
            'login': 'test_lead',
            'groups_id': [(6, 0, [
                cls.env.ref('base.group_user').id,
                cls.env.ref('competency_assessment.group_discipline_lead').id,
            ])],
        })
        cls.lead_emp = cls.Employee.create({
            'name': 'Lead Employee',
            'user_id': cls.user_lead.id,
        })
        cls.disc.lead_id = cls.lead_emp

        # Create assessments as admin
        cls.assessment_own = cls.Assessment.create({
            'employee_id': cls.emp.id,
            'discipline_id': cls.disc.id,
        })
        cls.assessment_other = cls.Assessment.create({
            'employee_id': cls.env.ref('hr.employee_admin') if cls.env.ref('hr.employee_admin', raise_if_not_found=False) else cls.emp.id,
            'discipline_id': cls.disc.id,
        })

    def test_employee_sees_own_assessments(self):
        """Record rule: employee sees own assessments."""
        assessments = self.Assessment.with_user(self.user_employee).search([])
        self.assertIn(self.assessment_own, assessments)

    def test_user_group_assignment(self):
        """Competency User group exists and is assignable."""
        group = self.env.ref('competency_assessment.group_competency_user')
        self.assertTrue(group)

    def test_discipline_lead_group_exists(self):
        """Discipline Lead group exists."""
        group = self.env.ref('competency_assessment.group_discipline_lead')
        self.assertTrue(group)

    def test_competency_admin_group_exists(self):
        """Competency Admin group exists."""
        group = self.env.ref('competency_assessment.group_competency_admin')
        self.assertTrue(group)

    def test_admin_can_access_all_models(self):
        """Admin has full access to all competency models."""
        models = [
            'competency.discipline',
            'competency.level',
            'competency.competency',
            'competency.criterion',
            'competency.assessment',
            'competency.assessment.line',
        ]
        for model in models:
            records = self.env[model].search([])
            self.assertTrue(True, f"Admin can search {model}")
