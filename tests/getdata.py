import requests
import unittest
from unittest import mock 

from main import get_data

def mocked_request_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        def json(self):
            return self.json_data
    yield MockResponse('',404)
    yield MockResponse('',404)
    yield MockResponse('',404)
    yield MockResponse("{'A':'B'}", 200)   

class TestGetData(unittest.TestCase):
    def test_OK(self):
        self.assertIsNotNone(get_data("http://www.mocky.io/v2/5e539b332e00007c002dacbe"))
    
    @mock.patch('requests.get', side_effect=mocked_request_get())
    def test_retries(self, mock_get):
        with self.assertLogs() as cm:
            self.assertIsNone(get_data("http://www.mocky.io/v2/5e81ea2b2f00000d002fb6d2",max_retries=1))
            self.assertIsNotNone(get_data("http://www.mocky.io/v2/5e81ea2b2f00000d002fb6d2"))
        self.assertEqual(len(cm.output),3)    
        
if __name__ == '__main__':
    unittest.main()



