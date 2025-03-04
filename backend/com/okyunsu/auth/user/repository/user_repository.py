from sqlalchemy.orm import Session
from com.okyunsu.auth.user.model.user_entity import UserEntity as User

# 사용자 추가
def add_user(db: Session, user_id: str, email: str, password: str, name: str):
    new_user = User(user_id=user_id, email=email, password=password, name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 모든 사용자 조회
def get_all_users(db: Session):
    return db.query(User).all()
