from flask import Blueprint, jsonify, request
from services.user_service import UserService
from dto.user_dto import UserDTO

user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    users_dto = [UserDTO.from_entity(user).__dict__ for user in users]
    return jsonify(users_dto), 200


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(UserDTO.from_entity(user).__dict__), 200
    return jsonify({"message": "User not found"}), 404


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = UserService.create_user(name=data['name'], email=data['email'])
    return jsonify(UserDTO.from_entity(user).__dict__), 201


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if UserService.delete_user(user_id):
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404
