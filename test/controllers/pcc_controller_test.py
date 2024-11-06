import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_company_request, build_consumer_request_1, build_pcc_request_1, \
    build_consumer_request_2


class CompanyConsumerPccControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.company = build_company_request(self.faker)
        self.consumer = build_consumer_request_1(self.faker, random)
        self.consumer2 = build_consumer_request_1(self.faker, random)
        self.pcc_1 = build_pcc_request_1(self.faker)
        with app.app_context():
            db.create_all()

    def test_get_pcc_success(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        pcc = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        response = self.test_client.get(
            f"/pccs/{json.loads(pcc.get_data())['id']}",
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 200)

    def test_get_pcc_not_found(self):
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            "/pccs/not-found",
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 404)

    def test_get_pcc_error(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        pcc = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer2),
            headers={'Content-Type': 'application/json'})
        token2 = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer2),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.get(
            f"/pccs/{json.loads(pcc.get_data())['id']}",
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token2.get_data())['token']}"})
        self.assertEqual(response.status_code, 409)
