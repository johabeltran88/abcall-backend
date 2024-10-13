from src.commons.exception_enum import ExceptionEnum
from src.commons.role_enum import RolesEnum
from src.exceptions.api_exception import ApiException
from src.models import AgentRole
from src.models.agent import Agent
from src.repositories.agent_repository import AgentRepository


class AgentService:

    @staticmethod
    def create_agent(agent: Agent):
        agent.roles.append(AgentRole(RolesEnum.AGENT.value, agent))
        return AgentRepository.create(agent)

    @staticmethod
    def login_agent(email, password):
        agent = AgentRepository.get_by_email(email)
        if not (agent and agent.check_password(password)):
            raise ApiException(ExceptionEnum.INVALID_CREDENTIALS)
        else:
            return agent
