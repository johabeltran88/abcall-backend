from enum import Enum


class ExceptionEnum(Enum):
    INVALID_CREDENTIALS = (401, 'INVALID_CREDENTIALS', 'Credenciales inválidas')
    BAD_REQUEST = (402, 'BAD_REQUEST', 'Campos obligatorios no estan presentes en la petición')

    def __init__(self, http_code, error_code, error_message):
        self.http_code = http_code
        self.error_code = error_code
        self.error_message = error_message
