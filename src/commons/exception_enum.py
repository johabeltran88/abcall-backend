from enum import Enum


class ExceptionEnum(Enum):
    UNAUTHORIZED = (401, 'UNAUTHORIZED', 'Credenciales inválidas', 'Invalid credentials')
    UNAUTHORIZED_WITHOUT_TOKEN = (401, 'UNAUTHORIZED', 'Token no enviado', 'Token not sent')
    UNAUTHORIZED_EXPIRED_TOKEN = (401, 'UNAUTHORIZED', 'Token expirado', 'Token expired')
    UNAUTHORIZED_INVALID_TOKEN = (401, 'UNAUTHORIZED', 'Token inválido', 'Invalid token')
    FORBIDDEN = (403, 'FORBIDDEN', 'Acceso prohibido', 'Access forbidden')
    BAD_REQUEST_MANDATORY = (402, 'BAD_REQUEST', 'Campos obligatorios no estan presentes en la petición',
                             'Mandatory fields are missing in the request')
    BAD_REQUEST_LENGTH = (402, 'BAD_REQUEST', 'Campos con longitud mínima o máxima inválida',
                          'Fields have invalid minimum or maximum length')
    INVALID_EMAIL = (409, 'CONFLICT', 'El correo electrónico ya se encuentra registrado',
                     'The email is already registered')
    INVALID_IDENTIFICATION = (409, 'CONFLICT', 'El tipo y número de identificación ya se encuentra registrado',
                              'The identification type and number are already registered')
    INVALID_COMPANY_CLIENT = (409, 'CONFLICT', 'El consumidor ya esta asociado a la empresa',
                              'The consumer is already associated with the company')
    COMPANY_NOT_FOUND = (404, 'NOT_FOUND', 'Compañia no encontrada', 'Company not found')
    CONSUMER_NOT_FOUND = (404, 'NOT_FOUND', 'Consumidor no encontrado', 'Consumer not found')
    CLIENT_NOT_FOUND = (404, 'NOT_FOUND', 'Cliente no encontrado', 'Client not found')
    AGENT_NOT_FOUND = (404, 'NOT_FOUND', 'Asesor no encontrado', 'Agent not found')
    PCC_NOT_FOUND = (404, 'NOT_FOUND', 'PQR no encontrado', 'PCC not found')
    PCC_NOT_BELONG_TO_CLIENT = (409, 'CONFLICT', 'El PQR no pertenece al consumidor',
                                'The PCC does not belong to the consumer')

    def __init__(self, http_code, error_code, error_message, en_error_message):
        self.http_code = http_code
        self.error_code = error_code
        self.error_message = error_message
        self.en_error_message = en_error_message
