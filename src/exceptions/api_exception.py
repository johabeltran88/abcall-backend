from flask import jsonify, request


class ApiException(Exception):
    def __init__(self, exception):
        self.http_code = exception.http_code
        self.error_code = exception.error_code
        self.error_message = exception.error_message
        self.en_error_message = exception.en_error_message
        super().__init__(self.error_message)

    def to_response(self):
        language = request.headers.get('Language', '').lower()
        response = {
            'error_code': self.error_code,
            'error_message': self.en_error_message if 'en' in language else self.error_message
        }
        return jsonify(response), self.http_code
