from src.commons.exception_enum import ExceptionEnum
from src.exceptions.bad_request_exception import BadRequestException


class ValidationUtil:
    @staticmethod
    def validate_not_blank(request, *fields):
        missing_fields = []
        for field in fields:
            if field not in request.json or not request.json[field]:
                missing_fields.append(field)
        if missing_fields:
            raise BadRequestException(ExceptionEnum.BAD_REQUEST, missing_fields)
