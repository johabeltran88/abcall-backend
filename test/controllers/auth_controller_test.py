import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_consumer_request_1, build_agent_or_client_request


class AuthControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.agent = build_agent_or_client_request(self.faker)
        self.client = build_agent_or_client_request(self.faker)
        self.consumer = build_consumer_request_1(self.faker, random)
        with app.app_context():
            db.create_all()

    def test_login_agent_success(self):
        self.test_client.post(
            '/agents',
            data=json.dumps(self.agent),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/agents/token',
            data=json.dumps(self.agent),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_agent_error(self):
        response = self.test_client.post(
            '/auth/agents/token',
            data=json.dumps(self.agent),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_client_success(self):
        self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/clients/token',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_client_error(self):
        response = self.test_client.post(
            '/auth/clients/token',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_consumer_success(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['token'])

    def test_login_consumer_error(self):
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 401)

    def test_login_without_fields_error(self):
        invalid = {}
        response = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(invalid),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 402)
