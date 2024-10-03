from flask import Blueprint, make_response

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health():
    return make_response('Service up !', 200)
