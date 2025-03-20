from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService

class UpdateCustomer(AbstractService):
    async def handle(self, db: AsyncSession, user_id: str, update_customer: CustomerSchema):
        pass

class PartialUpdateCustomer(AbstractService):
    async def handle(self, db: AsyncSession, user_id: str, update_customer: CustomerSchema):
        pass


