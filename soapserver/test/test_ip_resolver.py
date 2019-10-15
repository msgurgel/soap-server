import unittest
from soapserver.services.ip import ip_resolver as ipr

class IPResolverTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_resolve_ip_resolves_ip(self):
        actual = ipr.resolveIP("35.185.82.132")
        expected = ipr.IPInfo(None, 'VA', 'United States', None, 38.6582, -77.2497)

        self.assertDictEqual(expected.__dict__, actual.__dict__)

    def test_resolve_ip_doesnt_die_with_invalid_ip(self):
        with self.assertRaises(Exception) as e:
            ipr.resolveIP("bananas")

        the_exception = e.exception
        self.assertEqual("Invalid IP address", the_exception.args[0])

    def test_validate_ip_validates(self):
        valid_actual = ipr.validateIp("192.168.0.1")
        valid_expected = True

        invalid_actual = ipr.validateIp("bananas")
        invalid_expected = False

        self.assertEqual(valid_expected, valid_actual)
        self.assertEqual(invalid_expected, invalid_actual)


if __name__ == '__main__':
    unittest.main()