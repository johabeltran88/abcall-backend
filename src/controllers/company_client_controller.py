from flask import Blueprint, jsonify

from src.services.company_client_service import CompanyClientService

company_client_bp = Blueprint('company_client', __name__)


@company_client_bp.route('/companies/<company_id>/clients/<client_id>', methods=['POST'])
def add_client_to_company(company_id, client_id):
    client = CompanyClientService.add_client_to_company(company_id, client_id)
    return jsonify(client.to_dict()), 200
