import unittest
from data_structures.datacenter import Datacenter

class TestDataCenter(unittest.TestCase):
    def test_all_ok(self):
        d = Datacenter('Berlin', { 'BER-100' : {'networks': {}, 'security_level': 1}})
        self.assertIsInstance(d,Datacenter)
        d.remove_invalid_clusters()
        self.assertIs(len(d.clusters),1)
    def test_invalid_prefix(self):
        with self.assertLogs() as cm:
            d = Datacenter('Berlin', { 'XBER-100' : {'networks': {}, 'security_level': 1}})
            self.assertIsInstance(d,Datacenter)
            d.remove_invalid_clusters()
            self.assertEqual(len(d.clusters),0)
        self.assertEqual(len(cm.output),1)
        self.assertRegex(cm.output[0],r'removing .* from')
        
    def test_invalid_digits(self):
        with self.assertLogs() as cm:
            d = Datacenter('Berlin', { 'BER-1000' : {'networks': {}, 'security_level': 1}})
            self.assertIsInstance(d,Datacenter)
            d.remove_invalid_clusters()
            self.assertEqual(len(d.clusters),0)
        self.assertEqual(len(cm.output),1)
        self.assertRegex(cm.output[0],r'removing .* from')
        