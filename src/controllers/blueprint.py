from src.controllers.agent_controller import agent_bp
from src.controllers.auth_controller import auth_bp
from src.controllers.client_controller import client_bp
from src.controllers.company_client_controller import company_client_bp
from src.controllers.company_consumer_controller import company_consumer_bp
from src.controllers.company_consumer_pcc_controller import company_consumer_pcc_bp
from src.controllers.company_controller import company_bp
from src.controllers.consumer_controller import consumer_bp
from src.controllers.health_controller import health_bp


def register_blueprint(app):
    app.register_blueprint(agent_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(company_client_bp)
    app.register_blueprint(company_consumer_bp)
    app.register_blueprint(company_consumer_pcc_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(consumer_bp)
    app.register_blueprint(health_bp)
