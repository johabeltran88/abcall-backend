from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.repositories.client_repository import ClientRepository
from src.repositories.company_repository import CompanyRepository


class CompanyClientService:

    @staticmethod
    def add_client_to_company(company_id, client_id):
        company = CompanyRepository.get_by_id(company_id)
        if not company:
            raise ApiException(ExceptionEnum.COMPANY_NOT_FOUND)
        client = ClientRepository.get_by_id(client_id)
        if not client:
            raise ApiException(ExceptionEnum.CLIENT_NOT_FOUND)
        client.company_id = company.id
        ClientRepository.add_company()
        return client


