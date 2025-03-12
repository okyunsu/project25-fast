from com.okyunsu.account.leadership.director.service.update_service import UpdateService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema


class FullUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_director: DirectorSchema):                
        pass


class PartialUpdateStrategy(UpdateService):
    async def update(self, db: AsyncSession, user_id: str, update_director: DirectorSchema):                
        pass