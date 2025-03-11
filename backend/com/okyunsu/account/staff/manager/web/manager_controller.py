from com.okyunsu.account.staff.manager.web.manager_factory import ManagerFactory
from com.okyunsu.account.staff.manager.strategy.strategy_type import StrategyType


class ManagerController():
    def __init__(self):
        pass

    async def create_manager(self, **kwargs):
        return await ManagerFactory.execute(strategy=StrategyType.DEFAULT_CREATE, method="create", **kwargs)

    async def update_manager(self, **kwargs):
        return await ManagerFactory.execute(strategy=StrategyType.DEFAULT_UPDATE, method="update", **kwargs)

    async def delete_manager(self, **kwargs):
        return await ManagerFactory.execute(strategy=StrategyType.DEFAULT_DELETE, method="delete", **kwargs) 
    
    async def get_manager_detail(self, **kwargs):
        return await ManagerFactory.execute(strategy=StrategyType.GET_DETAIL, method="retrieve", **kwargs)

    async def get_manager_list(self, **kwargs):
            return await ManagerFactory.execute(strategy=StrategyType.GET_ALL, method="retrieve", **kwargs)
    
    
    
