from flask import Blueprint, request, make_response
from flask_jwt_extended import create_access_token

from src.commons.validation_util import ValidationUtil
from src.services.agent_service import AgentService
from src.services.client_service import ClientService
from src.services.consumer_service import ConsumerService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/agents/token', methods=['POST'])
def agent_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    agent = AgentService.login_agent(request.json['email'], request.json['password'])
    return make_response(__build_token(agent.id, agent.to_dict()['roles'])), 200


@auth_bp.route('/auth/consumers/token', methods=['POST'])
def consumer_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    consumer = ConsumerService.login_consumer(request.json['email'], request.json['password'])
    return make_response(__build_token(consumer.id, consumer.to_dict()['roles'])), 200


@auth_bp.route('/auth/clients/token', methods=['POST'])
def client_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    client = ClientService.login_client(request.json['email'], request.json['password'])
    return make_response(__build_token(client.id, client.to_dict()['roles'])), 200


def __build_token(user_id, roles):
    return {'token': create_access_token(identity=user_id, additional_claims={"roles": roles})}
