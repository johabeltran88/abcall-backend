from flask import Blueprint, request, make_response
from flask_jwt_extended import create_access_token

from src.commons.validation_util import ValidationUtil
from src.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/agents/token', methods=['POST'])
def agent_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    agent = AuthService.login_agent(request.json['email'], request.json['password'])
    return make_response(__build_token(agent.id, "agent", agent.to_dict()['roles'])), 200


@auth_bp.route('/auth/consumers/token', methods=['POST'])
def consumer_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    consumer = AuthService.login_consumer(request.json['email'], request.json['password'])
    return make_response(__build_token(consumer.id, "consumer", consumer.to_dict()['roles'])), 200


@auth_bp.route('/auth/clients/token', methods=['POST'])
def client_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    client = AuthService.login_client(request.json['email'], request.json['password'])
    return make_response(__build_token(client.id, "client", client.to_dict()['roles'])), 200


def __build_token(user_id, type, roles):
    return {'token': create_access_token(identity=user_id, additional_claims={f"{type}_id": user_id, "roles": roles})}
