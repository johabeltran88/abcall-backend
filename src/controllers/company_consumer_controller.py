from flask import Blueprint, jsonify

from src.services.company_consumer_service import CompanyConsumerService

company_consumer_bp = Blueprint('company_consumer', __name__)


@company_consumer_bp.route('/companies/<company_id>/consumers/<consumer_id>', methods=['POST'])
def add_consumer_to_company(company_id, consumer_id):
    consumer = CompanyConsumerService.add_consumer_to_company(company_id, consumer_id)
    return jsonify(consumer.to_dict()), 200
