from flask import Blueprint, request, make_response

from src.commons.validation_util import ValidationUtil
from src.services.agent_service import AgentService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/token/agents', methods=['POST'])
def agent_login():
    ValidationUtil.validate_not_blank(request, 'email', 'password')
    AgentService.login_agent(request.json['email'], request.json['password'])
    return make_response('OK'), 200
