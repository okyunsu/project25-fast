from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema

class UpdateService(ABC):
    @abstractmethod
    async def update(self, db: AsyncSession, user_id: str, update_director: DirectorSchema):
        pass



