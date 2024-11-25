from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class Pcc(db.Model, BaseModel):
    __tablename__ = 'pccs'
    subject = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    consumer_id = db.Column(db.String(36), db.ForeignKey('consumers.id'), nullable=False)
    company_id = db.Column(db.String(36), db.ForeignKey('companies.id'), nullable=True)
    agent_id = db.Column(db.String(36), db.ForeignKey('agents.id'), nullable=True)
    consumer = relationship('Consumer', back_populates='pccs')
    company = relationship('Company', back_populates='pccs')
    agent = relationship('Agent', back_populates='pccs')
    notifications = relationship('Notification', back_populates='pcc')

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
            'status': self.status,
            'company': self.company.to_dict() if self.company else None
        }

    def to_dict_with_consumer_and_company(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'description': self.description,
            'create_at': self.created_at,
            'status': self.status,
            'consumer': self.consumer.to_dict_2() if self.consumer else None,
            'company': self.company.to_dict() if self.company else None
        }

    def to_dict_with_consumer_and_company_and_notifications(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'description': self.description,
            'create_at': self.created_at,
            'status': self.status,
            'consumer': self.consumer.to_dict_2() if self.consumer else None,
            'company': self.company.to_dict() if self.company else None,
            'notifications': [notification.to_dict_with_roles_and_companies_and_pccs() for notification in sorted(
                self.notifications,
                key=lambda notification: notification.created_at,
                reverse=True
            )],
        }
