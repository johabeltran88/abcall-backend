import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db


class ConsumerControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        with app.app_context():
            db.create_all()

    def test_create_consumer_success(self):
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
        response = self.test_client.post(
            '/consumers',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertEqual(consumer['name'], json.loads(response.get_data())['name'])
        self.assertEqual(consumer['identification_type'], json.loads(response.get_data())['identification_type'])
        self.assertEqual(consumer['identification_number'], json.loads(response.get_data())['identification_number'])
        self.assertEqual(consumer['contact_number'], json.loads(response.get_data())['contact_number'])
        self.assertEqual(consumer['email'], json.loads(response.get_data())['email'])
        self.assertEqual(consumer['address'], json.loads(response.get_data())['address'])
        self.assertIsNotNone(json.loads(response.get_data())['create_at'])

    def test_create_consumer_invalid_email(self):
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
            '/consumers',
            data=json.dumps(consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 422)