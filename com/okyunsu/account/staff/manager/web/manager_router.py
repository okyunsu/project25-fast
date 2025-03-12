from fastapi import APIRouter, Depends

from com.okyunsu.account.staff.manager.web.manager_controller import ManagerController
from com.okyunsu.utils.creational.builder.db_builder import get_db



router = APIRouter()
controller = ManagerController()

@router.post("/create")
async def create_manager(db=Depends(get_db)):
    return await controller.create_manager(db=db)

@router.put("/update")
async def update_manager(db=Depends(get_db)):
    return await controller.update_manager(db=db)  

@router.delete("/delete")
async def delete_manager(db=Depends(get_db)):
    return await controller.delete_manager(db=db)

@router.get("/detail")
async def get_manager_detail(db=Depends(get_db)):
    return await controller.get_manager_detail(db=db)

@router.get("/list")
async def get_manager_list(db=Depends(get_db)):
    return await controller.get_manager_list(db=db)

    
