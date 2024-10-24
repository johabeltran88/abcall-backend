from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class Company(db.Model, BaseModel):
    __tablename__ = 'companies'
    name = db.Column(db.String(200), nullable=False)
    consumers = relationship('Consumer', secondary='companies_consumers', back_populates='companies')
    clients = relationship('Client', back_populates='company')
    pccs = relationship('Pcc', back_populates='company')

    def __init__(self, name):
        BaseModel.__init__(self)
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
