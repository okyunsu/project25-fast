from sqlalchemy import Column, String
from com.okyunsu.auth.user.repository.database import Base

# User 테이블 모델
class UserEntity(Base):
    __tablename__ = "users"
    
    user_id = Column(String(15), primary_key=True)
    email = Column(String(20), unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    name = Column(String(10), nullable=False)
