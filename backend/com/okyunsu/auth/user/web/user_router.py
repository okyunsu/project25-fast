
from fastapi import APIRouter, Depends
from pytest import Session
from com.okyunsu.auth.user.repository.database import SessionLocal
from com.okyunsu.auth.user.repository.user_repository import get_all_users
from com.okyunsu.auth.user.web.user_controller import UserController


router = APIRouter()
controller = UserController()

@router.get(path='/')
async def home_user():
    return controller.hello_user()




# DB 세션 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 모든 사용자 조회 API
@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)