from com.okyunsu.account.leadership.director.web.director_factory import DirectorFactory
from com.okyunsu.account.leadership.director.strategy.strategy_type import StrategyType


class DirectorController():
    def __init__(self):
        pass

    async def create_director(self, **kwargs):
        return await DirectorFactory.execute(strategy=StrategyType.DEFAULT_CREATE, method="create", **kwargs)

    async def update_director(self, **kwargs):
        return await DirectorFactory.execute(strategy=StrategyType.DEFAULT_UPDATE, method="update", **kwargs)

    async def delete_director(self, **kwargs):
        return await DirectorFactory.execute(strategy=StrategyType.DEFAULT_DELETE, method="delete", **kwargs)

    async def get_director_detail(self, **kwargs):
        return await DirectorFactory.execute(strategy=StrategyType.GET_DETAIL, method="retrieve", **kwargs)
    
    async def get_director_list(self, **kwargs):
        return await DirectorFactory.execute(strategy=StrategyType.GET_ALL, method="retrieve", **kwargs)

