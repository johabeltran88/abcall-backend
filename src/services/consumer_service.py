from src.commons.exception_enum import ExceptionEnum
from src.commons.role_enum import RolesEnum
from src.exceptions.api_exception import ApiException
from src.models.consumer_role import ConsumerRole
from src.repositories.consumer_repository import ConsumerRepository


class ConsumerService:

    @staticmethod
    def create_consumer(consumer):
        consumer_tmp = ConsumerRepository.get_by_email(consumer.email)
        if consumer_tmp:
            raise ApiException(ExceptionEnum.INVALID_EMAIL)
        consumer_tmp = ConsumerRepository.get_by_identification(consumer.identification_type,
                                                                consumer.identification_number)
        if consumer_tmp:
            raise ApiException(ExceptionEnum.INVALID_IDENTIFICATION)
        consumer.roles.append(ConsumerRole(RolesEnum.CONSUMER.value, consumer))
        return ConsumerRepository.create(consumer)

    @staticmethod
    def login_consumer(email, password):
        consumer = ConsumerRepository.get_by_email(email)
        if not (consumer and consumer.check_password(password)):
            raise ApiException(ExceptionEnum.INVALID_CREDENTIALS)
        return consumer

    @staticmethod
    def get_consumer_by_identification(identification_type, identification_number):
        consumer = ConsumerRepository.get_by_identification(identification_type, identification_number)
        if consumer:
            raise ApiException(ExceptionEnum.CONSUMER_NOT_FOUND)
        return consumer
