from src.config.database_config import db
from src.models.company import Company


class CompanyRepository:

    @staticmethod
    def create(company):
        db.session.add(company)
        db.session.commit()
        return company

    @staticmethod
    def get_by_id(company_id):
        return Company.query.filter_by(id=company_id).first()
