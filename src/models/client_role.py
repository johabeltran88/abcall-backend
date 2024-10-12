import os

from sqlalchemy import UUID, String
from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class ClientRole(db.Model, BaseModel):
    __tablename__ = 'clients_roles'
    name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                          db.ForeignKey('clients.id'), nullable=False)
    client = relationship('Client', back_populates='roles')

    def __init__(self, name, client_id):
        BaseModel.__init__(self)
        self.name = name
        self.client_id = client_id

    def to_dict(self):
        return self.name
