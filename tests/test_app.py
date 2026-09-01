import unittest
from app.app import app

class BasicAppTests(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"healthy", response.data)

if __name__ == '__main__':
    unittest.main()
