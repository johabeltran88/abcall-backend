import os
import uuid

from sqlalchemy import UUID, String

from src.config.database_config import db


class CompanyConsumer(db.Model):
    __tablename__ = 'companies_consumers'
    company_id = db.Column(String(36), db.ForeignKey('companies.id'), nullable=False, primary_key=True)
    consumer_id = db.Column(String(36), db.ForeignKey('consumers.id'), nullable=False, primary_key=True)
