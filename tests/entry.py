from data_structures.entry import Entry
import unittest

class TestEntry(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(Entry('192.168.1.1',False,'30/01/20 18:30:30'),Entry)
    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            Entry('192.168.1.1',False,'90/01/20 18:30:30')