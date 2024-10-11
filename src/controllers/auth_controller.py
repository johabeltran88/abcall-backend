from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/token/agents', methods=['POST'])
def agent_login():
    return None