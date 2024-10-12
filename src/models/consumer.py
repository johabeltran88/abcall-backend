from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_user import User


class Consumer(db.Model, User):
    __tablename__ = 'consumers'
    identification_type = db.Column(db.String(50), nullable=False)
    identification_number = db.Column(db.String(20), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    roles = relationship('ConsumerRole', back_populates='consumer')

    def __init__(self, name, email, password, identification_type, identification_number, contact_number, address):
        User.__init__(self, name, email, password)
        self.identification_type = identification_type
        self.identification_number = identification_number
        self.contact_number = contact_number
        self.address = address

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'identification_type': self.identification_type,
            'identification_number': self.identification_number,
            'contact_number': self.contact_number,
            'email': self.email,
            'address': self.address,
            'create_at': self.created_at,
            'roles': [role.to_dict() for role in self.roles]
        }

