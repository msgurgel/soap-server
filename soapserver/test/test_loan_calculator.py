from __future__ import division
import unittest
from soapserver.services.loan import loan_calculator as lc

class LoanCalculatorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_loan_payment_calculates_monthly_payment_amount(self):
        actual = lc.loanPayment(150000, 8 / 1200, 360)
        expected = 1100.65

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()