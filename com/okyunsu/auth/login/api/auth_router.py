from fastapi import APIRouter, Depends, Body, Response, Cookie, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.builder.db_builder import get_db
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.api.auth_controller import AuthController
from com.okyunsu.auth.login.services.token_service import TokenService
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
    response: Response,
    login_data: LoginRequest = Body(...),
    db: AsyncSession = Depends(get_db)
):
    result = await controller.login(login_data=login_data, db=db)
    
    if result.success and result.refresh_token:
        # Refresh Token을 httpOnly 쿠키로 설정
        response.set_cookie(
            key="refresh_token",
            value=result.refresh_token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", 7)) * 24 * 60 * 60,
            path="/api/auth"
        )
        result.refresh_token = None
    
    return result

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        key="refresh_token",
        path="/api/auth",
        httponly=True,
        secure=True,
        samesite="lax"
    )
    return {"success": True, "message": "로그아웃 되었습니다."}

@router.post("/refresh")
async def refresh_token(
    response: Response,
    refresh_token: str = Cookie(None, alias="refresh_token")
):
    # 토큰 갱신 서비스 호출
    result = await token_service.handle(refresh_token=refresh_token)
    
    # 새로운 Refresh Token을 쿠키에 설정
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", 7)) * 24 * 60 * 60,
        path="/api/auth"
    )
    
    # refresh_token은 쿠키로만 전송하므로 응답에서 제거
    result.pop("refresh_token")
    return result

