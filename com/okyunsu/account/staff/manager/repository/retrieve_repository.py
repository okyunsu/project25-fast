from com.okyunsu.account.staff.manager.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession

class RetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass

class DefaultRetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass
