
from fastapi import APIRouter, Depends

from com.okyunsu.account.guest.customer.web.customer_controller import CustomerController
from com.okyunsu.utils.creational.builder.db_builder import get_db


router = APIRouter()
controller = CustomerController()


@router.post("/create")
async def create_customer(db=Depends(get_db)):
    return await controller.create_customer(db=db)

@router.put("/update")
async def update_customer(db=Depends(get_db)):
    return await controller.update_customer(db=db)

@router.delete("/delete")
async def delete_customer(db=Depends(get_db)):
    return await controller.delete_customer(db=db)

@router.get("/detail")
async def get_customer_detail(db=Depends(get_db)):
    return await controller.get_customer_detail(db=db)

@router.get("/list")
async def get_customer_list(db=Depends(get_db)):
    print("🕞🕞get_customer_list 정보:", db)
    return await controller.get_customer_list(db=db)




