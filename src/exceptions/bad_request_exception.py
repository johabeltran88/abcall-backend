from src.exceptions.api_exception import ApiException


class BadRequestException(ApiException):
    def __init__(self, exception, fields):
        super().__init__(exception)
        self.fields = fields
