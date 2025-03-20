from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService

class DefaultDeleteRepository(AbstractService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        print("🐮🐮DefaultDeleteRepository 정보:", new_customer)


class ValidDeleteRepository(AbstractService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        pass
