from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.account.guest.customer.storages.get_customer import get_all_customer
from sqlalchemy.exc import SQLAlchemyError

class FindCustomers(AbstractService):
    async def handle(self, db: AsyncSession, **kwargs):
        pass
