import os

from sqlalchemy import UUID, String
from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class Pcc(db.Model, BaseModel):
    __tablename__ = 'pcss'
    subject = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    consumer_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                            db.ForeignKey('consumers.id'), nullable=False)
    company_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                           db.ForeignKey('companies.id'), nullable=True)
    consumer = relationship('Consumer', back_populates='pccs')
    company = relationship('Company', back_populates='pccs')

    def __init__(self, subject, description):
        BaseModel.__init__(self)
        self.subject = subject
        self.description = description
        self.status = 'Registrado'

    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'description': self.description,
            'create_at': self.created_at,
            'consumer': self.consumer.to_dict() if self.consumer else None,
            'company': self.company.to_dict() if self.company else None
        }
