from fastapi import APIRouter

from com.okyunsu.account.guest.customer.web.customer_router import router as customer_router
from com.okyunsu.account.staff.manager.web.manager_router import router as manager_router
from com.okyunsu.account.leadership.director.web.director_router import router as director_router

router = APIRouter()

router.include_router(customer_router, prefix='/customer')
router.include_router(manager_router, prefix='/manager')
router.include_router(director_router, prefix='/director')