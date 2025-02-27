from abc import ABCMeta, abstractmethod


class AbstractAdmin(metaclass = ABCMeta):
    
    @abstractmethod
    def hendle(self, **kwargs):
        pass
