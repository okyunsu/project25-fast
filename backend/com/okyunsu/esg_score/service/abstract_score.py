from abc import ABCMeta, abstractmethod


class AbstractScore(mataclass = ABCMeta):
    
    @abstractmethod
    def hendle(self, **kwargs):
        pass
