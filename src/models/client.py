from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_user import User


class Client(db.Model, User):
    __tablename__ = 'clients'
    roles = relationship('ClientRole', back_populates='client')

    def __init__(self, name, email, password):
        User.__init__(self, name, email, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'create_at': self.created_at,
            'roles': [role.to_dict() for role in self.roles]
        }