import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, upgrade

from src.config.database_config import init_db, db
from src.config.jwt_config import init_jwt
from src.controllers.blueprint import register_blueprint
from src.exceptions.error_handler import register_error_handler

app = Flask(__name__)
init_db(app)
Migrate(app, db)
init_jwt(app)
register_blueprint(app)
register_error_handler(app)
CORS(app)

if __name__ == '__main__':
    with app.app_context():
        if os.environ.get('DB_URI', None) is None:
            db.create_all()
        else:
            upgrade()
    app.run(host="0.0.0.0", port=5000, debug=True)
