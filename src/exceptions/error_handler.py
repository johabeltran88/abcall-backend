from flask import make_response, request

from src.exceptions.api_exception import ApiException
from src.exceptions.bad_request_exception import BadRequestException


def handle_api_exception(exception):
    return make_response({
        'error_code': exception.error_code,
        'error_message': get_message(exception),
    }), exception.http_code


def handle_bad_request_exception(exception):
    return make_response({
        'error_code': exception.error_code,
        'error_message': get_message(exception),
        'fields': exception.fields
    }), exception.http_code


def get_message(exception):
    language = request.headers.get('Language', '').lower()
    return exception.en_error_message if 'en' in language else exception.error_message


def register_error_handler(app):
    app.register_error_handler(ApiException, handle_api_exception)
    app.register_error_handler(BadRequestException, handle_bad_request_exception)