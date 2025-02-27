from fastapi import APIRouter

from com.okyunsu.auth.admin.web.admin_controller import AdminController


router = APIRouter()
controller = AdminController()

@router.get(path='/')
async def home_user():
    return controller.hello_user()


