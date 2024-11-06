from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.services.client_pcc_service import ClientPccService

client_pcc_bp = Blueprint('client_pcc', __name__)


@client_pcc_bp.route('/clients/pccs', methods=['GET'])
@roles_required('CLIENT')
def get_pccs_by_client():
    pccs = ClientPccService.get_pccs_by_client(get_jwt().get("client_id"))
    return jsonify([pcc.to_dict_with_consumer_and_company() for pcc in pccs]), 200
