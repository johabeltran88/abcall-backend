from flask import Blueprint, request, jsonify

from src.commons.roles_enum import RolesEnum
from src.models import Role
from src.models.agent import Agent
from src.services.agent_service import AgentService

agent_bp = Blueprint('agent', __name__)


@agent_bp.route('/agents', methods=['POST'])
def create_agent():
    agent = Agent(request.json['name'], request.json['email'], request.json['password'])
    agent.roles.append(Role(RolesEnum.AGENT.value, agent))
    agent = AgentService.create_agent(agent)
    return jsonify(agent.to_dict()), 201
