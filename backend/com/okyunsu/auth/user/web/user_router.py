
from fastapi import APIRouter
from com.okyunsu.auth.user.web.user_controller import UserController


router = APIRouter()
controller = UserController()

@router.get(path='/')
async def home_user():
    return controller.hello_user()


