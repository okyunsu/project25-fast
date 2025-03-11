from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from com.okyunsu.account.guest.customer.model.customer_schema import CustomerSchema

class UpdateService(ABC):
    @abstractmethod
    def update(self, db: AsyncSession, user_id: str, update_customer: CustomerSchema):
        pass
