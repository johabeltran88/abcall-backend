from functools import wraps

from flask_jwt_extended import jwt_required, get_jwt

from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException


def roles_required(*required_roles):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            roles = claims.get('roles', [])
            if not any(role in roles for role in required_roles):
                raise ApiException(ExceptionEnum.FORBIDDEN)
            return f(*args, **kwargs)

        return wrapper

    return decorator
