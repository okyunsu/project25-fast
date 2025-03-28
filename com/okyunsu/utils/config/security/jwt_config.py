from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

class TokenUtils:
    # JWT 설정
    SECRET_KEY = os.getenv("JWT_ACCESS_SECRET_KEY", "your-access-secret-key-here")
    REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY", "your-refresh-secret-key-here")
    ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", 7))

    @classmethod
    def create_access_token(cls, user_id: str, name: str) -> str:
        """Access Token 생성"""
        payload = {
            "sub": user_id,
            "name": name,
            "iat": datetime.now(timezone.utc).timestamp(),
            "exp": (datetime.now(timezone.utc) + timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()
        }
        return jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def create_refresh_token(cls, user_id: str, name: str) -> str:
        """Refresh Token 생성"""
        payload = {
            "sub": user_id,
            "name": name,
            "iat": datetime.now(timezone.utc).timestamp(),
            "exp": (datetime.now(timezone.utc) + timedelta(days=cls.REFRESH_TOKEN_EXPIRE_DAYS)).timestamp()
        }
        return jwt.encode(payload, cls.REFRESH_SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def decode_access_token(cls, token: str) -> dict:
        """Access Token 검증 및 디코드"""
        try:
            payload = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            return payload
        except JWTError:
            raise JWTError("Invalid access token")

    @classmethod
    def decode_refresh_token(cls, token: str) -> dict:
        """Refresh Token 검증 및 디코드"""
        try:
            payload = jwt.decode(token, cls.REFRESH_SECRET_KEY, algorithms=[cls.ALGORITHM])
            return payload
        except JWTError:
            raise JWTError("Invalid refresh token")