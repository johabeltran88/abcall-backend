from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.repositories.company_consumer_repository import CompanyConsumerRepository
from src.repositories.company_repository import CompanyRepository
from src.repositories.consumer_repository import ConsumerRepository


class CompanyConsumerService:

    @staticmethod
    def add_consumer_to_company(company_id, consumer_id):
        company = CompanyRepository.get_by_id(company_id)
        if not company:
            raise ApiException(ExceptionEnum.COMPANY_NOT_FOUND)
        consumer = ConsumerRepository.get_by_id(consumer_id)
        if not consumer:
            raise ApiException(ExceptionEnum.CONSUMER_NOT_FOUND)
        company_consumer = CompanyConsumerRepository.get_by_company_id_and_consumer_id(company_id, consumer_id)
        if company_consumer:
            raise ApiException(ExceptionEnum.INVALID_COMPANY_CLIENT)
        return ConsumerRepository.add_company(consumer, company)
