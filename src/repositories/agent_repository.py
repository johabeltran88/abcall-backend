from src.config.database import db
from src.models.agent import Agent


class AgentRepository:

    @staticmethod
    def create(agent: Agent):
        db.session.add(agent)
        db.session.commit()
        return agent

    @staticmethod
    def login(email: str, password: str):
        agent = Agent.query.filter_by(email=email).first()
        if agent and agent.check_password(password):
            return True
        else:
            return False
