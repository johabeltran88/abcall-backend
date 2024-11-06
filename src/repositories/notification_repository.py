from src.config.database_config import db


class NotificationRepository:

    @staticmethod
    def create(notification):
        db.session.add(notification)
        db.session.commit()
        return notification
