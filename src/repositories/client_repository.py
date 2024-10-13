from src.config.database_config import db
from src.models import Client


class ClientRepository:

    @staticmethod
    def create(client: Client):
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def get_by_email(email):
        return Client.query.filter_by(email=email).first()
