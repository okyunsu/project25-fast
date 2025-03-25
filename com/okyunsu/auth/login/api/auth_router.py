from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.builder.db_builder import get_db
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.api.auth_controller import AuthController

router = APIRouter(
    prefix="/auth",
)
controller = AuthController()

@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest = Body(...),
    db: AsyncSession = Depends(get_db)
):
    result = await controller.login(login_data=login_data, db=db)
    print("🎯🎯🎯🎯result : ", result)
    return result  # FastAPI가 자동으로 JSON으로 변환

@router.post("/logout")
async def logout():
    return {"success": True, "message": "로그아웃 되었습니다."} 