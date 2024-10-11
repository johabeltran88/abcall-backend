from flask import Flask, make_response
from src.config.database import init_db, db
from src.controllers.agent_controller import agent_bp
from src.controllers.auth_controller import auth_bp
from src.controllers.health_controller import health_bp
from src.exceptions.api_exception import ApiException
from src.exceptions.bad_request_exception import BadRequestException

app = Flask(__name__)
init_db(app)

app.register_blueprint(agent_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(health_bp)


@app.errorhandler(ApiException)
def handle_api_exception(exception):
    return (make_response({
        'error_code': exception.error_code,
        'error_message': exception.error_message,
    }), exception.http_code)

@app.errorhandler(BadRequestException)
def handle_bad_request_exception(exception):
    return make_response({
        'error_code': exception.error_code,
        'error_message': exception.error_message,
        'fields': exception.fields
    }), exception.http_code


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
