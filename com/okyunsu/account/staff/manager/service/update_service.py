from abc import ABC, abstractmethod

class UpdateService(ABC):
    @abstractmethod
    async def update(self, **kwargs):
        pass


