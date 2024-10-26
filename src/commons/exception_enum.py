from enum import Enum


class ExceptionEnum(Enum):
    UNAUTHORIZED = (401, 'UNAUTHORIZED', 'Credenciales inválidas')
    UNAUTHORIZED_WITHOUT_TOKEN = (401, 'UNAUTHORIZED', 'Token no enviado')
    UNAUTHORIZED_EXPIRED_TOKEN = (401, 'UNAUTHORIZED', 'Token expirado')
    UNAUTHORIZED_INVALID_TOKEN = (401, 'UNAUTHORIZED', 'Token inválido')
    FORBIDDEN = (403, 'FORBIDDEN', 'Acceso prohibido')
    BAD_REQUEST_MANDATORY = (402, 'BAD_REQUEST', 'Campos obligatorios no estan presentes en la petición')
    BAD_REQUEST_LENGTH = (402, 'BAD_REQUEST', 'Campos con longitud mínima o máxima inválida')
    INVALID_EMAIL = (409, 'CONFLICT', 'El correo electrónico ya se encuentra registrado')
    INVALID_IDENTIFICATION = (409, 'CONFLICT', 'El tipo y número de identificación ya se encuentra registrado')
    INVALID_COMPANY_CLIENT = (409, 'CONFLICT', 'El consumidor ya esta asociado a la empresa')
    COMPANY_NOT_FOUND = (404, 'NOT_FOUND', 'Compañia no encontrada')
    CONSUMER_NOT_FOUND = (404, 'NOT_FOUND', 'Consumidor no encontrado')
    CLIENT_NOT_FOUND = (404, 'NOT_FOUND', 'Cliente no encontrado')
    AGENT_NOT_FOUND = (404, 'NOT_FOUND', 'Asesor no encontrado')

    def __init__(self, http_code, error_code, error_message):
        self.http_code = http_code
        self.error_code = error_code
        self.error_message = error_message
