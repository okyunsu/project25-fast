from abc import ABC, abstractmethod

class CreateService(ABC):
    @abstractmethod
    async def create(self, **kwargs):
        pass
