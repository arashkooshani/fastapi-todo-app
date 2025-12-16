from sqlalchemy import Column, Integer, String,Text,func,Boolean,DateTime
from core.database import Base

class TaskModel(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    description =Column(Text(500),nullable=True)
    is_completed=Column(Boolean,default=False)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),server_onupdate=func.now())

