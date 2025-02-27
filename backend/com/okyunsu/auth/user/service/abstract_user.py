
from abc import ABCMeta, abstractmethod


class AbstractUser( metaclass = ABCMeta ):

    @abstractmethod
    def handle(slef, **kwargs): 
        pass
