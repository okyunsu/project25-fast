from com.okyunsu.account.staff.manager.service.update_service import UpdateService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.staff.manager.model.manager_schema import ManagerSchema


class FullUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_manager: ManagerSchema):
        pass

class PartialUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_manager: ManagerSchema):
        pass

