from flask import Blueprint, request, jsonify

from src.commons.validation_util import ValidationUtil
from src.models import Client
from src.services.client_service import ClientService

client_bp = Blueprint('client', __name__)


@client_bp.route('/clients', methods=['POST'])
def create_agent():
    ValidationUtil.validate_not_blank(request, 'name', 'email', 'password')
    client = Client(request.json['name'], request.json['email'], request.json['password'])
    client = ClientService.create_client(client)
    return jsonify(client.to_dict()), 201
