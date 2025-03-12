from com.okyunsu.account.leadership.director.service.create_service import CreateService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema


class DefaultCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_director: DirectorSchema):
        pass


class ValidCreateStrategy(CreateService):
    async def create(self, db: AsyncSession, new_director: DirectorSchema):
        pass