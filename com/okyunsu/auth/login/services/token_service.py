from fastapi import HTTPException
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.utils.config.security.jwt_config import TokenUtils

class TokenService(AbstractService):
    async def handle(self, **kwargs):
        try:
            refresh_token = kwargs.get("refresh_token")
            
            if not refresh_token:
                raise HTTPException(
                    status_code=401,
                    detail="Refresh token not found"
                )
            
            # Refresh Token 검증
            payload = TokenUtils.decode_refresh_token(refresh_token)
            user_id = payload.get("sub")
            name = payload.get("name")
            
            if not user_id or not name:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid refresh token"
                )
            
            # 새로운 토큰 생성
            new_access_token = TokenUtils.create_access_token(user_id, name)
            new_refresh_token = TokenUtils.create_refresh_token(user_id, name)
            
            return {
                "success": True,
                "access_token": new_access_token,
                "refresh_token": new_refresh_token,
                "message": "Token refreshed successfully"
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token"
            ) 