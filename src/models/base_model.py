import os
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Column, String
from sqlalchemy.dialects.postgresql import UUID


class BaseModel:
    id = Column(UUID(as_uuid=True) if os.environ.get('DB_URI', None) is None else String,
                primary_key=True,
                default=uuid.uuid4 if os.environ.get('DB_URI', None) is None else lambda: uuid.uuid4().hex)
    created_at = Column(DateTime, default=datetime.now())
