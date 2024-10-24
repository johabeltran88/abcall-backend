import json
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_agent_or_client_request


class ClientControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.client = build_agent_or_client_request(self.faker)
        with app.app_context():
            db.create_all()

    def test_create_client_success(self):
        response = self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertEqual(self.client['name'], json.loads(response.get_data())['name'])
        self.assertEqual(self.client['email'], json.loads(response.get_data())['email'])
        self.assertIsNotNone(json.loads(response.get_data())['create_at'])

    def test_create_client_invalid_email_error(self):
        self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 409)

    def test_get_client_by_token_success(self):
        self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/clients/token',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            "/clients",
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {json.loads(token.get_data())['token']}'})
        self.assertEqual(response.status_code, 200)
