from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.repositories.agent_repository import AgentRepository
from src.repositories.client_repository import ClientRepository
from src.repositories.consumer_repository import ConsumerRepository


class AuthService:

    @staticmethod
    def login_agent(email, password):
        agent = AgentRepository.get_by_email(email)
        if not (agent and agent.check_password(password)):
            raise ApiException(ExceptionEnum.UNAUTHORIZED)
        return agent

    @staticmethod
    def login_client(email, password):
        client = ClientRepository.get_by_email(email)
        if not (client and client.check_password(password)):
            raise ApiException(ExceptionEnum.UNAUTHORIZED)
        return client

    @staticmethod
    def login_consumer(email, password):
        consumer = ConsumerRepository.get_by_email(email)
        if not (consumer and consumer.check_password(password)):
            raise ApiException(ExceptionEnum.UNAUTHORIZED)
        return consumer
