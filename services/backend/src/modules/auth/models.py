from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.core.database import Base
from datetime import datetime, timezone

def _utcnow() -> datetime:
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime._utcnow)
    role = Column(String, default="user") # e.g., "admin", "analyst", "developer"