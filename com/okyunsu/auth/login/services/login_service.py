from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.repository import login_repository
from com.okyunsu.utils.config.security.jwt_config import TokenUtils
from com.okyunsu.utils.config.security.redis_config import RedisConfig
import os
from dotenv import load_dotenv

load_dotenv()

class LoginService(AbstractService):
    async def handle(self, **kwargs):
        try:
            print("🐮🐮🐮🐮Login 진입함")
            login_data = kwargs.get("login_data")
            db = kwargs.get("db")
            
            print("login_data : ", login_data)
            
            if not login_data:
                return LoginResponse(
                    success=False,
                    message="로그인 데이터가 필요합니다."
                )

            # 1단계: user_id 존재 여부 확인
            user_query, user_params = login_repository.get_user_query(login_data.user_id)
            user_result = await db.execute(user_query, user_params)
            user_exists = user_result.first()
            
            if not user_exists:
                return LoginResponse(
                    success=False,
                    message="존재하지 않는 사용자입니다."
                )

            # 2단계: 비밀번호 확인
            query, params = login_repository.get_login_query(login_data)
            result = await db.execute(query, params)
            user = result.first()
            
            if not user:
                return LoginResponse(
                    success=False,
                    message="비밀번호가 일치하지 않습니다."
                )

            # 3단계: JWT 토큰 생성
            access_token = TokenUtils.create_access_token(user.user_id, user.name)
            refresh_token = TokenUtils.create_refresh_token(user.user_id, user.name)

            # 4단계: Redis에 Refresh Token 저장
            await RedisConfig.set_refresh_token(
                user_id=user.user_id,
                refresh_token=refresh_token,
                expire_days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", 7))
            )

            # 5단계: 로그인 성공
            response = LoginResponse(
                success=True,
                message="로그인 성공",
                user_id=user.user_id,
                name=user.name,
                access_token=access_token,
                refresh_token=refresh_token
            )
            print("🎯🎯🎯🎯access_token : ", access_token)
            print("🎯🎯🎯🎯refresh_token : ", refresh_token)
            return response
            
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            return LoginResponse(
                success=False,
                message="시스템 오류가 발생했습니다."
            )






