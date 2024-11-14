from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.commons.validation_util import ValidationUtil
from src.models.notification import Notification
from src.services.pcc_service import PccService

pcc_bp = Blueprint('pcc', __name__)


@pcc_bp.route('/pccs/<pcc_id>', methods=['GET'])
@roles_required('AGENT', 'CONSUMER', 'CLIENT')
def get_pcc_by_id(pcc_id):
    pcc = PccService.get_pcc_by_id(pcc_id, get_jwt().get("consumer_id"))
    return jsonify(pcc.to_dict_with_consumer_and_company_and_notifications()), 200


@pcc_bp.route('/pccs/<pcc_id>', methods=['PUT'])
@roles_required('AGENT')
def update_pcc(pcc_id):
    ValidationUtil.validate_not_blank(request, 'status', 'reason')
    ValidationUtil.validate_length(request, {'name': 'reason', 'min': 8, 'max': 1000})
    notification = Notification(request.json['status'], request.json['reason'])
    pcc = PccService.update_pcc(pcc_id, notification)
    return jsonify(pcc.to_dict_with_consumer_and_company_and_notifications()), 200
