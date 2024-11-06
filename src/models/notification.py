from sqlalchemy import String
from sqlalchemy.orm import relationship

from src.config.database_config import db
from src.models.base_model import BaseModel


class Notification(db.Model, BaseModel):
    __tablename__ = 'notifications'
    status = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    pcc_id = db.Column(String(36), db.ForeignKey('pccs.id'))
    pcc = relationship('Pcc', back_populates='notifications')

    def __init__(self, status, reason):
        BaseModel.__init__(self)
        self.status = status
        self.reason = reason

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'reason': self.reason
        }
