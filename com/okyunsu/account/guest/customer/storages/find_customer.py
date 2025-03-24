from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

class RetrieveRepository(AbstractService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass