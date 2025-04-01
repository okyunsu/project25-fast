from fastapi import APIRouter, Depends, HTTPException, Security
from pydantic import BaseModel
from typing import List
from com.okyunsu.account.guest.customer.api.customer_controller import CustomerController
from com.okyunsu.utils.creational.builder.db_builder import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from fastapi.security import HTTPBearer
from com.okyunsu.utils.config.security.jwt_config import TokenUtils
from com.okyunsu.utils.config.security.redis_config import RedisConfig
from jose.exceptions import JWTError


router = APIRouter()
controller = CustomerController()
security = HTTPBearer()

async def verify_token(credentials = Security(security)):
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


@router.post("/create")
async def create_customer(new_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.create_customer(db=db, customer=new_customer)

@router.put("/update")
async def update_customer(db: AsyncSession = Depends(get_db)):
    return await controller.update_customer(db=db)

@router.delete("/delete/{user_id}")
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    print("🔍🔍 delete_customer 로 진입함")
    return await controller.delete_customer(db=db, user_id=user_id)

@router.get("/detail")
async def get_customer_detail(db: AsyncSession = Depends(get_db)):
    return await controller.get_customer_detail(db=db)

class CustomerListResponse(BaseModel):
    customer_list: List[CustomerSchema]


@router.get("/list", response_model=CustomerListResponse)
async def get_all_customer(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify_token)  # 토큰 검증은 list 엔드포인트에만 적용
):
    print("🎉🎉 get_customers 로 진입함")
    customers = await controller.get_customer_list(db=db)
    return {
        "customer_list": customers
    }

