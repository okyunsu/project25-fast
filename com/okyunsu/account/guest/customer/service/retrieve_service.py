from abc import ABC, abstractmethod

class RetrieveService(ABC):
    @abstractmethod
    async def retrieve(self, **kwargs):  
        pass