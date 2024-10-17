from src.commons.exception_enum import ExceptionEnum
from src.commons.role_enum import RolesEnum
from src.exceptions.api_exception import ApiException
from src.models import ClientRole
from src.repositories.client_repository import ClientRepository


class ClientService:

    @staticmethod
    def create_client(client):
        client_tmp = ClientRepository.get_by_email(client.email)
        if client_tmp:
            raise ApiException(ExceptionEnum.INVALID_EMAIL)
        client.roles.append(ClientRole(RolesEnum.CLIENT.value, client))
        return ClientRepository.create(client)

    @staticmethod
    def login_client(email, password):
        client = ClientRepository.get_by_email(email)
        if not (client and client.check_password(password)):
            raise ApiException(ExceptionEnum.INVALID_CREDENTIALS)
        else:
            return client
