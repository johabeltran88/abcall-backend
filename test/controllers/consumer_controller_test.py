import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_consumer_request_1, build_consumer_request_2


class ConsumerControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.consumer_1 = build_consumer_request_1(self.faker, random)
        self.consumer_2 = build_consumer_request_2(self.consumer_1, self.faker, random)
        with app.app_context():
            db.create_all()

    def test_create_consumer_success(self):
        response = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.validate_response(response)

    def test_create_consumer_invalid_email_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 409)

    def test_get_consumer_invalid_identification_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 409)

    def test_get_consumer_success(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}",
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.validate_response(response)

    def test_get_consumer_not_found_error(self):
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}",
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def validate_response(self, response):
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertEqual(self.consumer_1['name'], json.loads(response.get_data())['name'])
        self.assertEqual(self.consumer_1['identification_type'], json.loads(response.get_data())['identification_type'])
        self.assertEqual(self.consumer_1['identification_number'],
                         json.loads(response.get_data())['identification_number'])
        self.assertEqual(self.consumer_1['contact_number'], json.loads(response.get_data())['contact_number'])
        self.assertEqual(self.consumer_1['email'], json.loads(response.get_data())['email'])
        self.assertEqual(self.consumer_1['address'], json.loads(response.get_data())['address'])
        self.assertIsNotNone(json.loads(response.get_data())['create_at'])
