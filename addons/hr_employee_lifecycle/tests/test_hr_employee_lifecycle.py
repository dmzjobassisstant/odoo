from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestEmployee(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env['hr.employee'].create({
            'name': 'Test Employee',
            'employment_status': 'probation',
            'probation_end_date': '2026-06-30',
            'notice_period_days': 30,
            'bank_account': '12345678',
            'bank_sort_code': '12-34-56',
        })

    def test_employee_creation(self):
        """Test employee is created with probation status."""
        self.assertEqual(self.employee.employment_status, 'probation')
        self.assertEqual(self.employee.notice_period_days, 30)
        self.assertEqual(self.employee.bank_account, '12345678')

    def test_confirm_probation(self):
        """Test confirming probation moves employee to active."""
        self.employee.action_confirm_probation()
        self.assertEqual(self.employee.employment_status, 'active')

    def test_confirm_probation_already_active(self):
        """Test confirming probation on active employee raises error."""
        self.employee.employment_status = 'active'
        with self.assertRaises(UserError):
            self.employee.action_confirm_probation()

    def test_terminate_employment(self):
        """Test terminating employment."""
        self.employee.employment_status = 'active'
        self.employee.action_terminate_employment()
        self.assertEqual(self.employee.employment_status, 'terminated')

    def test_terminate_already_terminated(self):
        """Test terminating an already terminated employee raises error."""
        self.employee.employment_status = 'terminated'
        with self.assertRaises(UserError):
            self.employee.action_terminate_employment()

    def test_cron_probation_end(self):
        """Test cron job auto-confirms probation when end date reached."""
        self.env['hr.employee']._cron_check_probation_end()
        # Date is in the future, so employee should still be in probation
        self.assertEqual(self.employee.employment_status, 'probation')

        # Set end date to today
        from odoo import fields
        self.employee.probation_end_date = fields.Date.today()
        self.env['hr.employee']._cron_check_probation_end()
        self.assertEqual(self.employee.employment_status, 'active')


class TestContract(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env['hr.employee'].create({
            'name': 'Contract Test Employee',
            'employment_status': 'probation',
        })
        cls.contract = cls.env['hr.lifecycle.contract'].create({
            'name': 'Test Contract',
            'employee_id': cls.employee.id,
            'contract_type': 'permanent',
            'date_start': '2026-01-01',
            'wage': 50000,
            'notice_period_employer_days': 30,
            'notice_period_employee_days': 30,
            'statutory_redundancy_weeks': 4.0,
        })

    def test_contract_creation(self):
        """Test contract is created in draft state."""
        self.assertEqual(self.contract.state, 'draft')
        self.assertEqual(self.contract.contract_type, 'permanent')
        self.assertEqual(self.contract.wage, 50000)

    def test_activate_contract(self):
        """Test activating contract."""
        self.contract.action_activate()
        self.assertEqual(self.contract.state, 'active')
        # Employee should be moved to active from probation
        self.assertEqual(self.employee.employment_status, 'active')

    def test_terminate_contract(self):
        """Test terminating contract."""
        self.contract.state = 'active'
        self.contract.action_terminate()
        self.assertEqual(self.contract.state, 'terminated')

    def test_expire_contract(self):
        """Test expiring contract."""
        self.contract.state = 'active'
        self.contract.action_expire()
        self.assertEqual(self.contract.state, 'expired')

    def test_invalid_dates(self):
        """Test contract end date cannot be before start date."""
        self.contract.date_end = '2025-12-31'
        with self.assertRaises(UserError):
            self.contract._check_dates()


class TestOffboarding(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Ensure default tasks exist
        cls.employee = cls.env['hr.employee'].create({
            'name': 'Offboarding Test Employee',
            'employment_status': 'active',
        })
        cls.contract = cls.env['hr.lifecycle.contract'].create({
            'name': 'Offboarding Contract',
            'employee_id': cls.employee.id,
            'contract_type': 'permanent',
            'date_start': '2026-01-01',
            'wage': 60000,
            'statutory_redundancy_weeks': 3.0,
            'state': 'active',
        })

    def test_offboarding_creation(self):
        """Test creating an offboarding record."""
        offboarding = self.env['hr.offboarding'].create({
            'employee_id': self.employee.id,
            'offboarding_type': 'resignation',
            'initiated_by': 'employee',
            'reason': 'Better opportunity',
            'notice_given_date': '2026-06-01',
            'last_working_date': '2026-06-30',
        })
        self.assertEqual(offboarding.state, 'draft')
        self.assertTrue(offboarding.name.startswith('OFF'))

    def test_offboarding_workflow(self):
        """Test full offboarding workflow."""
        offboarding = self.env['hr.offboarding'].create({
            'employee_id': self.employee.id,
            'offboarding_type': 'resignation',
            'initiated_by': 'employee',
            'reason': 'Personal reasons',
        })

        # Start the process
        offboarding.action_start()
        self.assertEqual(offboarding.state, 'in_progress')
        # Default tasks should be created
        self.assertTrue(len(offboarding.task_ids) > 0)

        # Complete all tasks
        for task in offboarding.task_ids:
            task.action_complete()

        # Complete offboarding
        offboarding.action_complete()
        self.assertEqual(offboarding.state, 'completed')
        self.assertEqual(self.employee.employment_status, 'terminated')

    def test_cancel_offboarding(self):
        """Test cancelling offboarding."""
        offboarding = self.env['hr.offboarding'].create({
            'employee_id': self.employee.id,
            'offboarding_type': 'dismissal',
            'initiated_by': 'employer',
            'reason': 'Performance',
        })
        offboarding.action_start()
        offboarding.action_cancel()
        self.assertEqual(offboarding.state, 'cancelled')

    def test_cannot_complete_with_incomplete_tasks(self):
        """Test that offboarding cannot be completed with incomplete tasks."""
        offboarding = self.env['hr.offboarding'].create({
            'employee_id': self.employee.id,
            'offboarding_type': 'resignation',
            'initiated_by': 'employee',
        })
        offboarding.action_start()
        # Don't complete tasks
        with self.assertRaises(UserError):
            offboarding.action_complete()

    def test_settlement_calculation_redundancy(self):
        """Test settlement calculation for redundancy."""
        offboarding = self.env['hr.offboarding'].create({
            'employee_id': self.employee.id,
            'offboarding_type': 'redundancy',
            'initiated_by': 'employer',
            'contract_id': self.contract.id,
        })
        # Trigger onchange
        offboarding._onchange_calculate_settlement()
        expected_weekly = 60000 / 4.33
        expected = expected_weekly * 3.0
        self.assertAlmostEqual(offboarding.settlement_amount, expected, places=2)
        self.assertTrue(offboarding.settlement_breakdown)
