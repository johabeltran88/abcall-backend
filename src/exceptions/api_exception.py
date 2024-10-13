class ApiException(Exception):
    def __init__(self, exception):
        self.http_code = exception.http_code
        self.error_code = exception.error_code
        self.error_message = exception.error_message
        super().__init__(self.error_message)
