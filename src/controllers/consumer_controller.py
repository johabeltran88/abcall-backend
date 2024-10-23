from flask import request, jsonify, Blueprint

from src.commons.decorator import roles_required
from src.commons.validation_util import ValidationUtil
from src.models.consumer import Consumer
from src.services.consumer_service import ConsumerService

consumer_bp = Blueprint('consumer', __name__)


@consumer_bp.route('/consumers', methods=['POST'])
def create_consumer():
    ValidationUtil.validate_not_blank(request, 'name', 'email', 'password', 'identification_type',
                                      'identification_number', 'contact_number', 'address')
    consumer = Consumer(request.json['name'], request.json['email'], request.json['password'],
                        request.json['identification_type'], request.json['identification_number'],
                        request.json['contact_number'], request.json['address'])
    consumer = ConsumerService.create_consumer(consumer)
    return jsonify(consumer.to_dict()), 201


@consumer_bp.route('/consumers/identification_type/<identification_type>/identification_number/<identification_number>',
                   methods=['GET'])
@roles_required('AGENT', 'CONSUMER')
def get_consumer_by_identification(identification_type, identification_number):
    consumer = ConsumerService.get_consumer_by_identification(identification_type, identification_number)
    return jsonify(consumer.to_dict()), 200
