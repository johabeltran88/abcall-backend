from src.config.database_config import db
from src.models import Client


class ClientRepository:

    @staticmethod
    def create(client):
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def get_by_email(email):
        return Client.query.filter(Client.email.ilike(email)).first()

    @staticmethod
    def get_by_id(client_id):
        return Client.query.filter_by(id=client_id).first()

    @staticmethod
    def add_company():
        db.session.commit()
