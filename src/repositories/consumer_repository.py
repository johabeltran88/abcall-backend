from src.config.database_config import db
from src.models.consumer import Consumer


class ConsumerRepository:

    @staticmethod
    def create(consumer):
        db.session.add(consumer)
        db.session.commit()
        return consumer

    @staticmethod
    def get_by_email(email):
        return Consumer.query.filter(Consumer.email.ilike(email)).first()

    @staticmethod
    def get_by_identification(identification_type, identification_number):
        return Consumer.query.filter_by(identification_type=identification_type,
                                        identification_number=identification_number).first()

    @staticmethod
    def get_by_id(consumer_id):
        return Consumer.query.filter_by(id=consumer_id).first()

    @staticmethod
    def add_company(consumer, company):
        consumer.companies.append(company)
        db.session.commit()
        return consumer
