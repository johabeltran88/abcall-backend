import json
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_agent_or_client_request, build_company_request


class CompanyClientControllerTest(TestCase):

    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.company = build_company_request(self.faker)
        self.client = build_agent_or_client_request(self.faker)
        with app.app_context():
            db.create_all()

    def test_add_client_to_company(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        client = self.test_client.post(
            '/clients',
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/clients/{json.loads(client.get_data())['id']}",
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_add_client_to_company_company_not_found_error(self):
        response = self.test_client.post(
            f"/companies/error/clients/error",
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_add_client_to_company_client_not_found_error(self):
        company = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        response = self.test_client.post(
            f"/companies/{json.loads(company.get_data())['id']}/clients/error",
            data=json.dumps(self.client),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)
