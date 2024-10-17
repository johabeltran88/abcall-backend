import json
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db


class ClientControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        with app.app_context():
            db.create_all()

    def test_create_client_success(self):
        client = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'password': '123456'
        }
        response = self.test_client.post(
            '/clients',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertEqual(client['name'], json.loads(response.get_data())['name'])
        self.assertEqual(client['email'], json.loads(response.get_data())['email'])
        self.assertIsNotNone(json.loads(response.get_data())['create_at'])

    def test_create_client_invalid_email_error(self):
        client = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'password': '123456'
        }
        self.test_client.post(
            '/clients',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/clients',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 422)
