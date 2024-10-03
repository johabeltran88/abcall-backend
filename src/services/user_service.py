from src.repositories.user_repository import UserRepository
from src.models.user import User


class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)
        return UserRepository.create(new_user)

    @staticmethod
    def update_user(user_id, user):
        return UserRepository.update()

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
            return True
        return False
