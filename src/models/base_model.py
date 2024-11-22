import uuid
from datetime import datetime

from sqlalchemy import DateTime, Column, String


class BaseModel:
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now)
