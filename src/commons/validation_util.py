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
            raise BadRequestException(ExceptionEnum.BAD_REQUEST_MANDATORY, missing_fields)

    @staticmethod
    def validate_length(request, *fields):
        invalid_length_fields = []
        for field in fields:
            if not (field['min'] <= len(request.json[field['name']]) <= field['max']):
                invalid_length_fields.append(f"{field['name']} - min: {field['min']}, max: {field['max']}, current: {len(request.json[field['name']])}")
        if invalid_length_fields:
            raise BadRequestException(ExceptionEnum.BAD_REQUEST_LENGTH, invalid_length_fields)
