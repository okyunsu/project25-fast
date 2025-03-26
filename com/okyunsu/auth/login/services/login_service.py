from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.repository import login_repository

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

            # 1단계: 로그인 시도
            query, params = login_repository.get_login_query(login_data)
            result = await db.execute(query, params)
            user = result.first()
            
            if not user:
                return LoginResponse(
                    success=False,
                    message="아이디 또는 비밀번호가 일치하지 않습니다."
                )

            # 2단계: 로그인 성공
            response = LoginResponse(
                success=True,
                message="로그인 성공",
                user_id=user.user_id,
                name=user.name,
                token="dummy_token"
            )
            
            print("🎯🎯🎯🎯login result : ", response)
            return response
            
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            return LoginResponse(
                success=False,
                message="시스템 오류가 발생했습니다."
            )






