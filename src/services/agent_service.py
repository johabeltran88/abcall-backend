from src.models.agent import Agent
from src.repositories.agent_repository import AgentRepository


class AgentService:

    @staticmethod
    def create_agent(agent: Agent):
        agent
        return AgentRepository.create(agent)

    @staticmethod
    def login_agent(email: str, password: str):
        return AgentRepository.login(email, password)