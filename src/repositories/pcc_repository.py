from src.config.database_config import db
from src.models import Pcc


class PccRepository:

    @staticmethod
    def create(pcc):
        db.session.add(pcc)
        db.session.commit()
        return pcc

    @staticmethod
    def get_pccs(agent_id):
        return Pcc.query.filter_by(agent_id=agent_id).all()
