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

    def test_create_consumer_invalid_identification_error(self):
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
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}",
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {json.loads(token.get_data())['token']}'})
        self.assertEqual(response.status_code, 200)
        self.validate_response(response)

    def test_get_consumer_not_found_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}1",
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {json.loads(token.get_data())['token']}'})
        self.assertEqual(response.status_code, 404)

    def test_get_consumer_expired_token_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}1",
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyOTY1OTU4NCwianRpIjoiNTRjNzlhZjMtODM3OS00MDYwLTk1NGYtYzAyZWRkNzY3MWYzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQ4Mzk3MzlkMTkzNDQ3M2M5MjBiNmM0YmY3MDM1YzRkIiwibmJmIjoxNzI5NjU5NTg0LCJjc3JmIjoiZTJlMTNhMjUtZjI3Zi00ZjFkLWIwN2ItZWI0ODMyOGY0ODY1IiwiZXhwIjoxNzI5NjU5NTg1LCJjbGllbnRfaWQiOiI0ODM5NzM5ZDE5MzQ0NzNjOTIwYjZjNGJmNzAzNWM0ZCIsInJvbGVzIjpbIkNPTlNVTUVSIl19.DnmUYmFbaMSME3w4nvHO_4DHeY45IfEpHg4oW2e57EY'})
        self.assertEqual(response.status_code, 401)

    def test_get_consumer_invalid_token_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}1",
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer invalid'})
        self.assertEqual(response.status_code, 401)

    def test_get_consumer_without_token_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_2),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/consumers/identification_type/{self.consumer_1['identification_type']}/identification_number/{self.consumer_1['identification_number']}1",
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_get_client_by_token_success(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            "/consumers",
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {json.loads(token.get_data())['token']}'})
        self.assertEqual(response.status_code, 200)

    def test_get_client_by_token_with_invalid_role_error(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer_1),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            "/clients",
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {json.loads(token.get_data())['token']}'})
        self.assertEqual(response.status_code, 403)

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
