from com.okyunsu.account.staff.manager.service.delete_service import DeleteService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.staff.manager.model.manager_schema import ManagerSchema


class SoftDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_manager: ManagerSchema):
        pass


class HardDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_manager: ManagerSchema):
        pass