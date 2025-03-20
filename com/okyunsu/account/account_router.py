from fastapi import APIRouter

from com.okyunsu.account.guest.customer.api.customer_router import router as customer_router
from com.okyunsu.account.leadership.director.web.director_router import router as director_router

router = APIRouter()

router.include_router(customer_router, prefix='/customer')
router.include_router(director_router, prefix='/director')