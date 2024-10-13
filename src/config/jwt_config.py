from datetime import timedelta

from flask_jwt_extended import JWTManager


def init_jwt(app):
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    JWTManager(app)
