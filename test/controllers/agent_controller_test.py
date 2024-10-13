import json
from unittest import TestCase

from faker import Faker

from main import app


class AgentControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_agent_success(self):
        agent = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'password': '123456'
        }
        response = self.test_client.post(
            '/agents',
            data=json.dumps(agent),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertEqual(agent['name'], json.loads(response.get_data())['name'])
        self.assertEqual(agent['email'], json.loads(response.get_data())['email'])
        self.assertIsNotNone(json.loads(response.get_data())['create_at'])
