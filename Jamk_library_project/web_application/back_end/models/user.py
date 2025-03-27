from sqlalchemy import Column, Integer, String, Boolean
from back_end.db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default='student') # Default role is student
    is_active = Column(Boolean, default=True)