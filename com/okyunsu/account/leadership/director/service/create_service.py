from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema

class CreateService(ABC):
    @abstractmethod
    async def create(self, db: AsyncSession, new_director: DirectorSchema):
        pass




