from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED


class ServiceValidationError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.http_error_code = HTTP_422_UNPROCESSABLE_ENTITY
        self.errors = errors if errors is not None else []

    def to_json(self):
        return {
            'http_status': self.http_error_code,
            'messages': self.errors
        }


class BusinessLogicException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.http_error_code = HTTP_400_BAD_REQUEST
        self.errors = {
            "message": message,
            "fields": [],
            "error_code": 0,
        }

    def to_json(self):
        return {
            'data': self.errors
        }


class UnauthorizedError(Exception):
    def __init__(self, message='invalid authorization header'):
        super().__init__(message)
        self.http_error_code = HTTP_401_UNAUTHORIZED
        self.errors = {
            "message": message,
            "fields": [],
            "error_code": 0,
        }

    def to_json(self):
        return {
            'data': self.errors
        }
