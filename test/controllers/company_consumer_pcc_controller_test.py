import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_consumer_request_1, build_company_request, build_pcc_request_1, \
    build_pcc_request_2, build_pcc_request_3


class CompanyConsumerPccControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.company = build_company_request(self.faker)
        self.consumer = build_consumer_request_1(self.faker, random)
        self.pcc_1 = build_pcc_request_1(self.faker)
        self.pcc_2 = build_pcc_request_2(self.faker)
        self.pcc_3 = build_pcc_request_3(self.faker)
        with app.app_context():
            db.create_all()

    def test_create_pcc_success(self):
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
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 201)

    def test_create_pcc_subject_invalid_length_1(self):
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
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_2),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 402)

    def test_create_pcc_subject_invalid_length_2(self):
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
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_3),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 402)

    def test_create_pcc_company_not_found(self):
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/error/consumers/{json.loads(consumer.get_data())['id']}/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 404)

    def test_create_pcc_client_not_found(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        token = self.test_client.post(
            '/auth/consumers/token',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/error/pccs",
            data=json.dumps(self.pcc_1),
            headers={'Content-Type': 'application/json',
                     'Authorization': f"Bearer {json.loads(token.get_data())['token']}"})
        self.assertEqual(response.status_code, 404)
