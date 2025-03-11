from abc import ABC, abstractmethod

class DeleteService(ABC):
    @abstractmethod
    async def delete(self, **kwargs):
        pass

