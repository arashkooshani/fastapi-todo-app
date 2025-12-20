from sqlalchemy import Column, Integer, String,Text,func,Boolean,DateTime
from core.database import Base
from sqlalchemy.orm import relationship
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(250),nullable=False)
    password = Column(String, nullable=False)
    is_active=Column(Boolean,default=True)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),server_onupdate=func.now())
    tasks = relationship("TaskModel",back_populates="user")

    def hash_password(password: str) -> str:
        """
        Hash a plain-text password.
        """
        return pwd_context.hash(password)

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a password against its hash.
        """
        return pwd_context.verify(plain_password, hashed_password)

