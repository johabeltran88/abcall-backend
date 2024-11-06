import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_company_request, build_consumer_request_1, build_pcc_request_1, \
    build_agent_or_client_request


class ClientPccControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.client = build_agent_or_client_request(self.faker)
        self.company = build_company_request(self.faker)
        self.consumer = build_consumer_request_1(self.faker, random)
        self.pcc_1 = build_pcc_request_1(self.faker)
        with app.app_context():
            db.create_all()

    def test_get_pccs_success(self):
        client = self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/clients/{json.loads(client.get_data())['id']}",
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        token = self.test_client.post(
            '/auth/clients/token',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            "/clients/pccs",
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 200)
