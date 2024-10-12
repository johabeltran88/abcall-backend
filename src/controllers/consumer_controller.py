from flask import request, jsonify, Blueprint

from src.commons.validation_util import ValidationUtil
from src.models.consumer import Consumer
from src.services.consumer_service import ConsumerService

consumer_bp = Blueprint('consumer', __name__)


@consumer_bp.route('/consumers', methods=['POST'])
def create_agent():
    ValidationUtil.validate_not_blank(request, 'name', 'email', 'password', 'identification_type',
                                      'identification_number', 'contact_number', 'address')
    consumer = Consumer(request.json['name'], request.json['email'], request.json['password'],
                        request.json['identification_type'], request.json['identification_number'],
                        request.json['contact_number'], request.json['address'])
    consumer = ConsumerService.create_consumer(consumer)
    return jsonify(consumer.to_dict()), 201
