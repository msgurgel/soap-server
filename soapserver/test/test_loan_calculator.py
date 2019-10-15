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

    def test_loan_payment_throws_excep_when_payments_is_zero(self):
        with self.assertRaises(Exception) as e:
            lc.loanPayment(150000, 8 / 1200, 0)

        the_exception = e.exception
        self.assertEqual("Payments cannot be zero", the_exception.args[0])

if __name__ == '__main__':
    unittest.main()