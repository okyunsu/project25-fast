from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from com.okyunsu.account.leadership.director.model.director_schema import DirectorSchema

class DeleteService(ABC):
    @abstractmethod
    async def delete(self, db: AsyncSession, user_id: str, new_director: DirectorSchema):
        pass




