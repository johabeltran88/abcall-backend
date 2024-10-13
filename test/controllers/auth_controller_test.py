import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db


class AuthControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        with app.app_context():
            db.create_all()

    def test_login_agent_success(self):
        agent = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'password': '123456'
        }
        self.test_client.post(
            '/agents',
            data=json.dumps(agent),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/agents/token',
            data=json.dumps(agent),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_agent_error(self):
        agent = {
            'email': 'test@test.com',
            'password': '123456'
        }
        response = self.test_client.post(
            '/auth/agents/token',
            data=json.dumps(agent),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_client_success(self):
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
            '/auth/clients/token',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_client_error(self):
        client = {
            'email': 'test@test.com',
            'password': '123456'
        }
        self.test_client.post(
            '/clients',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/clients/token',
            data=json.dumps(client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_consumer_success(self):
        consumer = {
            'name': self.faker.name(),
            'identification_type': random.choice(["Cédula de ciudadanía", "Cédula de extranjería",
                                                  "Tarjeta de identidad", "Pasaporte"]),
            'identification_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
            'contact_number': ''.join([str(random.randint(1, 9)) for _ in range(10)]),
            'email': self.faker.email(),
            'address': self.faker.address(),
            'password': '123456'
        }
        self.test_client.post(
            '/consumers',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_consumer_error(self):
        consumer = {
            'email': 'test@test.com',
            'password': '123456'
        }
        self.test_client.post(
            '/consumers',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_without_fields_error(self):
        invalid = {}
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(invalid),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 402)
