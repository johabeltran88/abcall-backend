from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.models.notification import Notification
from src.repositories.agent_repository import AgentRepository
from src.repositories.company_repository import CompanyRepository
from src.repositories.consumer_repository import ConsumerRepository
from src.repositories.notification_repository import NotificationRepository
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
        agent = AgentRepository.get_random()
        pcc.company_id = company.id
        pcc.consumer_id = consumer.id
        pcc.agent_id = agent.id
        pcc = PccRepository.create(pcc)
        notification1 = Notification('Registrado', 'El PQR ha sido registrado exitosamente')
        notification1.pcc_id = pcc.id
        NotificationRepository.create(notification1)
        notification2 = Notification('Registrado', 'El PQR ha sido asigando a un asesor')
        notification2.pcc_id = pcc.id
        NotificationRepository.create(notification2)
        return pcc
