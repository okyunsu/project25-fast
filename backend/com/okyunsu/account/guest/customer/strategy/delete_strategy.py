from com.okyunsu.account.guest.customer.service.delete_service import DeleteService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.model.customer_schema import CustomerSchema

class SoftDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        pass


class HardDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        pass    

