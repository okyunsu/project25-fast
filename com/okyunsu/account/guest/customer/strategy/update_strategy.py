from com.okyunsu.account.guest.customer.service.update_service import UpdateService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.model.customer_schema import CustomerSchema
    

class FullUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_customer: CustomerSchema):
        pass

class PartialUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_customer: CustomerSchema):
        pass


