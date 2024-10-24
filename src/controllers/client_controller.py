from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt

from src.commons.decorator import roles_required
from src.commons.validation_util import ValidationUtil
from src.models import Client
from src.services.client_service import ClientService

client_bp = Blueprint('client', __name__)


@client_bp.route('/clients', methods=['POST'])
def create_client():
    ValidationUtil.validate_not_blank(request, 'name', 'email', 'password')
    client = Client(request.json['name'], request.json['email'], request.json['password'])
    client = ClientService.create_client(client)
    return jsonify(client.to_dict()), 201


@client_bp.route('/clients', methods=['GET'])
@roles_required('CLIENT')
def get_consumer_by_token():
    consumer = ClientService.get_client_by_id(get_jwt().get("client_id"))
    return jsonify(consumer.to_dict()), 200
