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

            try:
                # login_data를 LoginRequest로 변환
                if isinstance(login_data, dict):
                    login_data = LoginRequest(**login_data)
            except Exception as e:
                print(f"[ERROR] Invalid login data: {e}")
                return LoginResponse(
                    success=False,
                    message="아이디와 비밀번호를 입력해주세요."
                )
            
            # 로그인 쿼리 실행
            query, params = login_repository.get_login_query(login_data)
            result = await db.execute(query, params)
            user = result.first()
            
            if not user:
                # 사용자 존재 여부 확인
                user_query, user_params = login_repository.get_user_query(login_data.user_id)
                user_result = await db.execute(user_query, user_params)
                user_exists = user_result.first()
                
                print("🎯🎯🎯🎯login result : None")
                
                if not user_exists:
                    return LoginResponse(
                        success=False,
                        message="존재하지 않는 사용자입니다."
                    )
                return LoginResponse(
                    success=False,
                    message="비밀번호가 일치하지 않습니다."
                )
            
            result = LoginResponse(
                success=True,
                message="로그인 성공",
                user_id=user.user_id,
                name=user.name,
                token="dummy_token"
            )
            
            print("🎯🎯🎯🎯login result : ", result)
            return result
            
        except Exception as e:
            print(f"[ERROR] Login failed: {e}")
            return LoginResponse(
                success=False,
                message="시스템 오류가 발생했습니다."
            )






