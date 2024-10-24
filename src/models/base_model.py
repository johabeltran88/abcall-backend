import os
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Column, String
from sqlalchemy.dialects.postgresql import UUID


class BaseModel:
    id = Column(String(36), primary_key=True, default=lambda : str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now())
