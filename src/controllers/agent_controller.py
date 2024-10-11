from flask import Blueprint, request, jsonify

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
