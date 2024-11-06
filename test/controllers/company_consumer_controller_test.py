import json
import random
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_company_request, build_consumer_request_1


class CompanyConsumerControllerTest(TestCase):

    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.company = build_company_request(self.faker)
        self.consumer = build_consumer_request_1(self.faker, random)
        with app.app_context():
            db.create_all()

    def test_add_consumer_to_company(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}",
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_add_consumer_to_company_company_not_found_error(self):
        response = self.test_client.post(
            f"/companies/error/consumers/error",
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_add_consumer_to_company_consumer_not_found_error(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/error",
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_add_consumer_to_company_error(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        consumer = self.test_client.post(
            '/consumers',
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}",
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/consumers/{json.loads(consumer.get_data())['id']}",
            data=json.dumps(self.consumer),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 409)
