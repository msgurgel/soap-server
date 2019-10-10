import unittest
from soapserver.services.case import case_converter as cc

class CaseConverterTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_converter_converts_to_uppercase(self):
        actual = cc.convertCase("hello", cc.Convert.toUpper)
        expected = "HELLO"

        self.assertEqual(expected, actual)

    def test_case_converter_converts_to_lowercase(self):
        actual = cc.convertCase("GOODBYE", cc.Convert.toLower)
        expected = "goodbye"

        self.assertEqual(expected, actual)

    def test_case_converter_raises_error_when_invalid_conversion_is_given(self):
        with self.assertRaises(Exception):
            cc.convertCase("won't covert", "banana")

if __name__ == '__main__':
    unittest.main()