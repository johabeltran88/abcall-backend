from datetime import timedelta

from flask_jwt_extended import JWTManager

from src.commons.exception_enum import ExceptionEnum
from src.exceptions.api_exception import ApiException


def init_jwt(app):
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def missing_token_callback(callback):
        return ApiException(ExceptionEnum.UNAUTHORIZED_WITHOUT_TOKEN).to_response()

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return ApiException(ExceptionEnum.UNAUTHORIZED_EXPIRED_TOKEN).to_response()

    @jwt.invalid_token_loader
    def invalid_token_callback(reason):
        return ApiException(ExceptionEnum.UNAUTHORIZED_INVALID_TOKEN).to_response()
