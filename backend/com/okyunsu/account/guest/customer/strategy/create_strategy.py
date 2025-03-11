from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.model.customer_schema import CustomerSchema
from com.okyunsu.account.guest.customer.repository.create_repository import DefaultCreateRepository
from com.okyunsu.account.guest.customer.service.create_service import CreateService

class DefaultCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_customer: CustomerSchema) :
        customer_repo = DefaultCreateRepository(db)
        return customer_repo.create(new_customer)


class ValidCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_customer: CustomerSchema) :
        pass




