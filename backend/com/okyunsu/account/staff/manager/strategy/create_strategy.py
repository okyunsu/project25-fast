from com.okyunsu.account.staff.manager.service.create_service import CreateService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.staff.manager.model.manager_schema import ManagerSchema


class DefaultCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_manager: ManagerSchema) :
        pass


class ValidCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_manager: ManagerSchema) :
        pass                
