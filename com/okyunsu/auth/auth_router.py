from fastapi import APIRouter

from com.okyunsu.auth.login.api.auth_router import router as login_router

router = APIRouter()


router.include_router(login_router)
