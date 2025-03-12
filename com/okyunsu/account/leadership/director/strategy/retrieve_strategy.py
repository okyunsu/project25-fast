from com.okyunsu.account.leadership.director.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.leadership.director.repository.retrieve_repository import RetrieveRepository



class GetAllStrategy(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        repository = RetrieveRepository() 
        return await repository.retrieve(db=db)  # await 추가


class GetDetailStrategy(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass


