from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.services.agent_pcc_service import AgentPccService

agent_pcc_bp = Blueprint('agent_pcc', __name__)


@agent_pcc_bp.route('/agents/pccs', methods=['GET'])
@roles_required('AGENT')
def get_pccs_by_agent():
    pccs = AgentPccService.get_pccs_by_agent(get_jwt().get("agent_id"))
    return jsonify([pcc.to_dict_with_consumer_and_company() for pcc in pccs]), 200
