from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from com.okyunsu.account.guest.customer.api.customer_controller import CustomerController
from com.okyunsu.utils.creational.builder.db_builder import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema


router = APIRouter()
controller = CustomerController()


@router.post("/create")
async def create_customer(new_customer: CustomerSchema, db:AsyncSession = Depends(get_db)):
    return await controller.create_customer(db=db, customer=new_customer)

@router.put("/update")
async def update_customer(db=Depends(get_db)):
    return await controller.update_customer(db=db)

@router.delete("/delete/{user_id}")
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    print("🔍🔍 delete_customer 로 진입함")
    return await controller.delete_customer(db=db, user_id=user_id)

@router.get("/detail")
async def get_customer_detail(db=Depends(get_db)):
    return await controller.get_customer_detail(db=db)

class CustomerListResponse(BaseModel):
    customer_list: List[CustomerSchema]


@router.get("/list", response_model=CustomerListResponse)
async def get_all_customer(db: AsyncSession = Depends(get_db)):
    print("🎉🎉 get_customers 로 진입함")
    customers = await controller.get_customer_list(db=db)
    return {
        "customer_list": customers
    }

