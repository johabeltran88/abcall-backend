from src.config.database_config import db


class PccRepository:

    @staticmethod
    def create(pcc):
        db.session.add(pcc)
        db.session.commit()
        return pcc
