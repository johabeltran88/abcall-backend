import json
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_agent_or_client_request


class AgentPccControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.agent = build_agent_or_client_request(self.faker)
        with app.app_context():
            db.create_all()

    def test_get_pcss_by_agent_success(self):
        self.test_client.post(
            '/agents',
            data=json.dumps(self.agent),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/agents/token',
            data=json.dumps(self.agent),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            '/agents/pccs',
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 200)

