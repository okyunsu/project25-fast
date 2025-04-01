from fastapi import APIRouter, Depends, Body, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.builder.db_builder import get_db
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.api.auth_controller import AuthController
from com.okyunsu.auth.login.services.token_service import TokenService
from com.okyunsu.utils.config.security.redis_config import RedisConfig
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/auth",
)
controller = AuthController()
token_service = TokenService()

@router.post("/login", response_model=LoginResponse)
async def login(
    login_data: LoginRequest = Body(...),
    db: AsyncSession = Depends(get_db)
):
    result = await controller.login(login_data=login_data, db=db)
    return result

@router.post("/logout")
async def logout(refresh_token: str = Body(...)):
    try:
        if refresh_token:
            # 토큰에서 user_id 추출
            payload = token_service.decode_refresh_token(refresh_token)
            user_id = payload.get("sub")
            
            if user_id:
                # Redis에서 토큰 삭제
                await RedisConfig.delete_refresh_token(user_id)
    except Exception as e:
        print(f"Error during logout: {e}")
    
    return {"success": True, "message": "로그아웃 되었습니다."}

@router.post("/refresh")
async def refresh_token(refresh_token: str = Body(...)):
    # 토큰 갱신 서비스 호출
    result = await token_service.handle(refresh_token=refresh_token)
    return result

