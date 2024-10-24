from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.commons.validation_util import ValidationUtil
from src.models.agent import Agent
from src.services.agent_service import AgentService

agent_bp = Blueprint('agent', __name__)


@agent_bp.route('/agents', methods=['POST'])
def create_agent():
    ValidationUtil.validate_not_blank(request, 'name', 'email', 'password')
    agent = Agent(request.json['name'], request.json['email'], request.json['password'])
    agent = AgentService.create_agent(agent)
    return jsonify(agent.to_dict()), 201


@agent_bp.route('/agents', methods=['GET'])
@roles_required('AGENT')
def get_agent_by_token():
    consumer = AgentService.get_agent_by_id(get_jwt().get("agent_id"))
    return jsonify(consumer.to_dict()), 20
