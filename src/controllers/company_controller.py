from flask import request, Blueprint, jsonify

from src.commons.validation_util import ValidationUtil
from src.models.company import Company
from src.services.company_service import CompanyService

company_bp = Blueprint('companny', __name__)


@company_bp.route('/companies', methods=['POST'])
def create_company():
    ValidationUtil.validate_not_blank(request, 'name')
    company = Company(request.json['name'])
    company = CompanyService.create_company(company)
    return jsonify(company.to_dict()), 201
