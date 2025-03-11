from com.okyunsu.account.common.user.model.user_entity import UserEntity
from com.okyunsu.account.guest.customer import repository
from com.okyunsu.account.guest.customer.repository.retrieve_repository import RetrieveRepository
from com.okyunsu.account.guest.customer.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession


class GetAllStrategy(RetrieveService):


    async def retrieve(self, db: AsyncSession, **kwargs):  # async 추가
        repository = RetrieveRepository() 
        return await repository.retrieve(db=db)  # await 추가
    
class GetDetailStrategy(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass




