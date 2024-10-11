from src.config.database import db
from src.models.base_user import User


class Client(db.Model, User):
    __tablename__ = 'clients'

    def __init__(self, name, email, password):
        User.__init__(self, name, email, password)
