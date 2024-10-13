from unittest import TestCase

from main import app


class HealthControllerTests(TestCase):
    def setUp(self):
        self.test_client = app.test_client()

    def test_health(self):
        response = self.test_client.get('/health')
        self.assertEqual(response.status_code, 200)
