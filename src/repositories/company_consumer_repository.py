from src.config.database_config import db
from src.models import CompanyConsumer


class CompanyConsumerRepository:

    @staticmethod
    def get_by_company_id_and_consumer_id(company_id, consumer_id):
        return db.session.query(CompanyConsumer).filter_by(company_id=company_id, consumer_id=consumer_id).first()
