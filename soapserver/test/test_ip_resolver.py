import unittest
from soapserver.services.ip import ip_resolver as ipr

class IPResolverTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_resolve_ip_resolves_ip(self):
        actual = ipr.resolveIP("35.185.82.132")
        expected = ipr.IPInfo(None, 'VA', 'United States', None, 38.6582, -77.2497)

        self.assertDictEqual(expected.__dict__, actual.__dict__)

if __name__ == '__main__':
    unittest.main()