from src.config.database_config import db
from src.models.agent import Agent


class AgentRepository:

    @staticmethod
    def create(agent: Agent):
        db.session.add(agent)
        db.session.commit()
        return agent

    @staticmethod
    def get_by_email(email):
        return Agent.query.filter_by(email=email).first()
