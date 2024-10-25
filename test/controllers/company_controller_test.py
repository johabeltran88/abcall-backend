import json
from unittest import TestCase

from faker import Faker

from main import app
from src.config.database_config import db
from test.controllers.requests import build_company_request


class CompanyControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()
        self.company = build_company_request(self.faker)
        with app.app_context():
            db.create_all()

    def test_create_company_success(self):
        response = self.test_client.post(
            '/companies',
            data=json.dumps(self.company),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
