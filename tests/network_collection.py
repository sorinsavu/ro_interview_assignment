import unittest
from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry

class TestNet(unittest.TestCase):
    def test_all_ok(self):
        n = NetworkCollection('192.168.0.0/24', [{'address': '192.168.0.1', 'available': False, 'last_used': "30/01/20 17:00:00"}])
        self.assertIsInstance(n, NetworkCollection)
        n.remove_invalid_records()
        self.assertIs(len(n.entries),1)
    def test_invalid_formats(self):
        with self.assertLogs() as cm:
            n = NetworkCollection('192.168.0.0/24', [{'address': '192.168.0.400', 'available': False, 'last_used': "30/01/20 17:00:00"},
                {'address': '192.168.400', 'available': False, 'last_used': "30/01/20 17:00:00"},
                {'address': 'invalid', 'available': False, 'last_used': "30/01/20 17:00:00"},
            ])
            self.assertIsInstance(n, NetworkCollection)
            n.remove_invalid_records()
            self.assertIs(len(n.entries),0)
        self.assertEqual(len(cm.output),3)
        self.assertRegex(cm.output[0], r'invalid')
    def test_outside_network(self):
        with self.assertLogs() as cm:
            n = NetworkCollection('192.168.0.0/24', [{'address': '192.168.1.1', 'available': False, 'last_used': "30/01/20 17:00:00"}])
            self.assertIsInstance(n, NetworkCollection)
            n.remove_invalid_records()
            self.assertIs(len(n.entries),0)
        self.assertEqual(len(cm.output),1)
        self.assertRegex(cm.output[0], r'ip .* not in')
    def test_sort(self):
        n = NetworkCollection('192.168.0.0/24', [{'address': '192.168.0.2', 'available': False, 'last_used': "30/01/20 17:00:00"},
            {'address': '192.168.0.1', 'available': False, 'last_used': "30/01/20 17:00:00"}])
        self.assertIsInstance(n, NetworkCollection)
        self.assertIs(n.entries[0].address,'192.168.0.2')
        n.sort_records()
        self.assertIs(n.entries[0].address, '192.168.0.1')

