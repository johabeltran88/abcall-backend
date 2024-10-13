import os

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class ConsumerRole(db.Model, BaseModel):
    __tablename__ = 'consumers_roles'
    name = db.Column(db.String(100), nullable=False)
    consumer_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                            db.ForeignKey('consumers.id'), nullable=False)
    consumer = relationship('Consumer', back_populates='roles')

    def __init__(self, name, consumer_id):
        BaseModel.__init__(self)
        self.name = name
        self.consumer_id = consumer_id

    def to_dict(self):
        return self.name
