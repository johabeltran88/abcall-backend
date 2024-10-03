from src.config.database import db
from src.models.base_model import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __init__(self, name, email):
        BaseModel.__init__(self)
        self.name = name
        self.email = email
