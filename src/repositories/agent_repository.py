from src.config.database_config import db
from src.models.agent import Agent
from sqlalchemy.sql.expression import func



class AgentRepository:

    @staticmethod
    def create(agent: Agent):
        db.session.add(agent)
        db.session.commit()
        return agent

    @staticmethod
    def get_by_email(email):
        return Agent.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(agent_id):
        return Agent.query.filter_by(id=agent_id).first()

    @staticmethod
    def get_random():
        return Agent.query.order_by(func.random()).first()
