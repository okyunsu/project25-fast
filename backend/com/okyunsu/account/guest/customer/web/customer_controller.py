

from com.okyunsu.account.guest.customer.strategy.strategy_type import StrategyType
from com.okyunsu.account.guest.customer.web.customer_factory import CustomerFactory


class CustomerController():
    def __init__(self):
        pass

    async def create_customer(self, **kwargs):
        return await CustomerFactory.execute(strategy=StrategyType.DEFAULT_CREATE, method="create", **kwargs)

    async def update_customer(self, **kwargs):
        return await CustomerFactory.execute(strategy=StrategyType.DEFAULT_UPDATE, method="update", **kwargs)

    async def delete_customer(self, **kwargs):
        return await CustomerFactory.execute(strategy=StrategyType.DEFAULT_DELETE, method="delete", **kwargs)

    async def get_customer_detail(self, **kwargs):
        return await CustomerFactory.execute(strategy=StrategyType.GET_DETAIL, method="retrieve", **kwargs)
  
    async def get_customer_list(self, **kwargs):
        return await CustomerFactory.execute(strategy=StrategyType.GET_ALL, method="retrieve",**kwargs)
