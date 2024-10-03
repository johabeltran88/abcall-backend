class UserDTO:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def from_entity(user):
        return UserDTO(name=user.name, email=user.email)

    def to_entity(self):
        return {
            "name": self.name,
            "email": self.email
        }
