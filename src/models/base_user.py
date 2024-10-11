from sqlalchemy import Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.base_model import BaseModel


class User(BaseModel):
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password_hash = Column(String(200), nullable=False)

    def __init__(self, name, email, password):
        BaseModel.__init__(self)
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
