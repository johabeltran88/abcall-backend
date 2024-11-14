from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException
from src.repositories.notification_repository import NotificationRepository
from src.repositories.pcc_repository import PccRepository


class PccService:

    @staticmethod
    def get_pcc_by_id(pcc_id, consumer_id):
        pcc = PccRepository.get_pcc_by_id(pcc_id)
        if not pcc:
            raise ApiException(ExceptionEnum.PCC_NOT_FOUND)
        if consumer_id and pcc.consumer_id != consumer_id:
            raise ApiException(ExceptionEnum.PCC_NOT_BELONG_TO_CLIENT)
        return pcc

    @staticmethod
    def update_pcc(pcc_id, notification):
        pcc = PccRepository.get_pcc_by_id(pcc_id)
        if not pcc:
            raise ApiException(ExceptionEnum.PCC_NOT_FOUND)
        PccRepository.update_status(pcc_id, notification.status)
        notification.pcc_id = pcc.id
        NotificationRepository.create(notification)
        return PccRepository.get_pcc_by_id(pcc_id)
