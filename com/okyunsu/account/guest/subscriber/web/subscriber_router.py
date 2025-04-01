from fastapi import APIRouter, Depends, HTTPException, Request, Security
from pydantic import BaseModel
from typing import List
from com.okyunsu.account.guest.subscriber.model.subscriber_schema import SubscriberSchema
from com.okyunsu.account.guest.subscriber.web.subscriber_controller import SubscriberController
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.config.security.jwt_config import TokenUtils
from com.okyunsu.utils.config.security.redis_config import RedisConfig
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv
from jose.exceptions import JWTError

from com.okyunsu.utils.creational.builder.db_builder import get_db

load_dotenv()

router = APIRouter()
controller = SubscriberController()
security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        token = credentials.credentials
        # JWT 토큰 검증
        payload = TokenUtils.decode_refresh_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        # Redis에서 토큰 검증
        stored_token = await RedisConfig.get_refresh_token(user_id)
        if not stored_token:
            raise HTTPException(status_code=401, detail="Token not found in Redis")
        if stored_token != token:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
            
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    except Exception as e:
        print(f"Redis error: {str(e)}")
        raise HTTPException(status_code=500, detail="Redis connection error")

@router.get("/list", response_model=List[SubscriberSchema])
async def get_all_subscribers(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify_token)
):
    print("🎉🎉 get_subscribers 로 진입함")
    subscribers = await controller.get_subscriber_list(db=db)
    return subscribers

@router.post("/create")
async def create_subscriber(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify_token)
):
    return await controller.create_subscriber(db=db)

@router.put("/update")
async def update_subscriber(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify_token)
):
    return await controller.update_subscriber(db=db)

@router.delete("/delete/{user_id}")
async def delete_subscriber(
    user_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(verify_token)
):
    return await controller.delete_subscriber(db=db, user_id=user_id)