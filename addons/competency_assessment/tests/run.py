#!/usr/bin/env python3
"""Standalone test runner for Competency Assessment module.
Works around the Odoo 19 namespace package issue by initializing Odoo 
and patching the addons path before test discovery.

Usage: docker exec odoo python3 /mnt/extra-addons/competency_assessment/tests/run.py
"""

import os
import sys
import unittest

# Add module parent to path and set up Odoo environment
EXTRA_ADDONS = '/mnt/extra-addons'
sys.path.insert(0, EXTRA_ADDONS)

# Initialize Odoo (this sets up the import hooks and registry)
import odoo
from odoo.tests import loader

# Patch the namespace path so Odoo's test loader can find our module
odoo.addons.__path__ = odoo.tools.config._NamespacePath(
    list(odoo.addons.__path__) + [EXTRA_ADDONS]
)

# Now discover tests from our module
from odoo.tests.common import TransactionCase, tagged

# Import test classes directly from our test file
from odoo.addons.competency_assessment.tests import (
    TestCompetencyDiscipline,
    TestCompetencyLevel,
    TestCompetencyCriteria,
    TestAssessmentWorkflow,
    TestCompetencySecurity,
)

def run_tests():
    """Discover and run all competency tests."""
    # Build test suite from our classes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    test_classes = [
        TestCompetencyDiscipline,
        TestCompetencyLevel,
        TestCompetencyCriteria,
        TestAssessmentWorkflow,
        TestCompetencySecurity,
    ]
    
    for cls in test_classes:
        tests = loader.loadTestsFromTestCase(cls)
        suite.addTests(tests)
    
    # Run
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print(f"\n{'='*70}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests())
