from fastapi import APIRouter, Depends
from com.okyunsu.utils.creational.builder.db_builder import get_db
from com.okyunsu.account.leadership.director.web.director_controller import DirectorController


router = APIRouter()
controller = DirectorController()


@router.post("/create")
async def create_director(db=Depends(get_db)):
    return await controller.create_director(db=db)

@router.put("/update")
async def update_director(db=Depends(get_db)):
    return await controller.update_director(db=db)


@router.delete("/delete")
async def delete_director(db=Depends(get_db)):
    return await controller.delete_director(db=db)

@router.get("/detail")
async def get_director_detail(db=Depends(get_db)):
    return await controller.get_director_detail(db=db)

@router.get("/list")
async def get_director_list(db=Depends(get_db)):
    return await controller.get_director_list(db=db)
