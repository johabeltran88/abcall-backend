import os

from sqlalchemy import UUID, String

from src.config.database_config import db


class CompanyConsumer(db.Model):
    __tablename__ = 'companies_consumers'
    company_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                           db.ForeignKey('companies.id'), nullable=False, primary_key=True)
    consumer_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                            db.ForeignKey('consumers.id'), nullable=False, primary_key=True)
