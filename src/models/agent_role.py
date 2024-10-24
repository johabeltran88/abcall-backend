import os

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class AgentRole(db.Model, BaseModel):
    __tablename__ = 'agents_roles'
    name = db.Column(db.String(100), nullable=False)
    agent_id = db.Column(String(36), db.ForeignKey('agents.id'), nullable=False)
    agent = relationship('Agent', back_populates='roles')

    def __init__(self, name, agent_id):
        BaseModel.__init__(self)
        self.name = name
        self.agent_id = agent_id

    def to_dict(self):
        return self.name
