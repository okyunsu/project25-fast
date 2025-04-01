import redis.asyncio as redis
import os
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=int(os.getenv("REDIS_DB", 0)),
        decode_responses=True
    )

    @classmethod
    async def set_refresh_token(cls, user_id: str, refresh_token: str, expire_days: int):
        """Refresh Token을 Redis에 저장"""
        key = f"refresh_token:{user_id}"
        await cls.redis_client.set(key, refresh_token)
        await cls.redis_client.expire(key, expire_days * 24 * 60 * 60)  # 초 단위로 변환

    @classmethod
    async def get_refresh_token(cls, user_id: str) -> str:
        """Redis에서 Refresh Token 조회"""
        key = f"refresh_token:{user_id}"
        return await cls.redis_client.get(key)

    @classmethod
    async def delete_refresh_token(cls, user_id: str):
        """Redis에서 Refresh Token 삭제"""
        key = f"refresh_token:{user_id}"
        await cls.redis_client.delete(key) 