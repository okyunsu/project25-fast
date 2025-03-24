from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.builder.db_builder import get_db
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.api.auth_controller import AuthController

router = APIRouter(prefix="/auth")
controller = AuthController()

@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    return await controller.login(db=db, login_data=login_data)

@router.post("/logout")
async def logout():
    return {"success": True, "message": "로그아웃 되었습니다."} 