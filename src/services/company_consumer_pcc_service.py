from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.repositories.company_repository import CompanyRepository
from src.repositories.consumer_repository import ConsumerRepository
from src.repositories.pcc_repository import PccRepository


class CompanyConsumerPccService:

    @staticmethod
    def create_pcc_to_consumer_of_company(company_id, consumer_id, pcc):
        company = CompanyRepository.get_by_id(company_id)
        if not company:
            raise ApiException(ExceptionEnum.COMPANY_NOT_FOUND)
        consumer = ConsumerRepository.get_by_id(consumer_id)
        if not consumer:
            raise ApiException(ExceptionEnum.CONSUMER_NOT_FOUND)
        pcc.company_id = company.id
        pcc.consumer_id = consumer.id
        return PccRepository.create(pcc)
