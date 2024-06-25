import unittest
import json
from main import app
    
class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_start_timer(self):
        response = self.app.get('/start')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('startTime', data)

    def test_stop_timer(self):
        response = self.app.get('/stop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'timer stopped')

    def test_continue_timer(self):
        response = self.app.get('/continue')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('startTime', data)


if __name__ == '__main__':
    unittest.main()