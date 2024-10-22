from flask import Blueprint, request, jsonify

from src.commons.validation_util import ValidationUtil
from src.models.pcc import Pcc
from src.services.company_consumer_pcc_service import CompanyConsumerPccService

company_consumer_pcc_bp = Blueprint('company_consumer_pcc', __name__)


@company_consumer_pcc_bp.route('/companies/<company_id>/consumers/<consumer_id>/pccs', methods=['POST'])
def create_pcc(company_id, consumer_id):
    ValidationUtil.validate_not_blank(request, 'subject', 'description')
    pcc = Pcc(request.json['subject'], request.json['description'])
    pcc = CompanyConsumerPccService.create_pcc_to_consumer_of_company(company_id, consumer_id, pcc)
    return jsonify(pcc.to_dict()), 201
