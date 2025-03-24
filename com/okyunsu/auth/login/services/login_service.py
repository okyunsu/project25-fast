from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.auth.login.models.login_schema import LoginRequest, LoginResponse
from com.okyunsu.auth.login.storages.login_repository import LoginRepository

class LoginService(AbstractService):
    async def handle(self, **kwargs):
        try:
            db: AsyncSession = kwargs.get("db")
            login_data: LoginRequest = kwargs.get("login_data")
            
            print("👉 로그인 시도:", {
                "user_id": login_data.user_id if login_data else None,
                "password": login_data.password if login_data else None
            })
            
            if not login_data:
                return LoginResponse(
                    success=False,
                    message="로그인 데이터가 필요합니다."
                )
            
            repository = LoginRepository()
            result = await repository.verify_login(db, login_data)
            
            if not result:
                return LoginResponse(
                    success=False,
                    message="아이디 또는 비밀번호가 일치하지 않습니다."
                )
                
            return LoginResponse(
                success=True,
                message="로그인 성공",
                user_id=result.get("user_id"),
                name=result.get("name"),
                token="dummy_token"  # 실제 구현에서는 JWT 토큰 생성
            )
        
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            return LoginResponse(
                success=False,
                message=f"로그인 처리 중 오류가 발생했습니다: {str(e)}"
            )






