from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService

class DeleteCustomer(AbstractService): 
    async def handle(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        pass


class RemoveCustomer(AbstractService):
    async def handle(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        pass    

