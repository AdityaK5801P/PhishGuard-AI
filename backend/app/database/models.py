from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.app.database.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String, nullable=False)

    prediction = Column(String, nullable=False)

    uses_https = Column(Boolean, default=False)

    contains_ip = Column(Boolean, default=False)

    contains_at_symbol = Column(Boolean, default=False)

    hyphen_count = Column(Integer, default=0)

    dot_count = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())