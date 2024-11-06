from src.config.database_config import db
from src.models import Pcc


class PccRepository:

    @staticmethod
    def create(pcc):
        db.session.add(pcc)
        db.session.commit()
        return pcc

    @staticmethod
    def get_pccs_by_agent_id(agent_id):
        return Pcc.query.filter_by(agent_id=agent_id).all()

    @staticmethod
    def get_pccs_by_company_id(company_id):
        return Pcc.query.filter_by(company_id=company_id).all()

    @staticmethod
    def get_pcc_by_id(pcc_id):
        return Pcc.query.filter_by(id=pcc_id).first()
