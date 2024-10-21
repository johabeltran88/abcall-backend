from src.config.database_config import db


class Company(db.Model):
    __tablename__ = 'companies'
    name = db.Column(db.String(200), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_dic(self):
        return {
            'id': self.id,
            'name': self.name
        }
