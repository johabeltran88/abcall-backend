from src.config.database_config import db
from src.models.consumer import Consumer


class ConsumerRepository:

    @staticmethod
    def create(consumer: Consumer):
        db.session.add(consumer)
        db.session.commit()
        return consumer

    @staticmethod
    def get_by_email(email):
        return Consumer.query.filter_by(email=email).first()
