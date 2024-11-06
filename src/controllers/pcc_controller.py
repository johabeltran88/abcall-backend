from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.services.client_service import ClientService
from src.services.pcc_service import PccService

pcc_bp = Blueprint('pcc', __name__)


@pcc_bp.route('/pccs/<pcc_id>', methods=['GET'])
@roles_required('AGENT', 'CONSUMER', 'CLIENT')
def get_pcc_by_id(pcc_id):
    pcc = PccService.get_pcc_by_id(pcc_id, get_jwt().get("consumer_id"))
    return jsonify(pcc.to_dict_with_consumer_and_company_and_notifications()), 200
