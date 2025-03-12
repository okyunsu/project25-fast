from com.okyunsu.account.leadership.director.service.delete_service import DeleteService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema


class SoftDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_director: DirectorSchema):
        pass


class HardDeleteStrategy(DeleteService):
    async def delete(self, db: AsyncSession, user_id: str, new_director: DirectorSchema):
        pass