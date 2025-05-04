import unittest
import sys
from Tests.test_input_submission import TestInputSubmission

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestInputSubmission))
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(run_tests())