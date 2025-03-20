from com.okyunsu.account.guest.customer.models.customer_action import CustomerAction
from com.okyunsu.account.guest.customer.api.customer_factory import CustomerFactory


class CustomerController():
    def __init__(self):
        pass

    async def create_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.CREATE_CUSTOMER, **kwargs)

    async def update_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.UPDATE_CUSTOMER, **kwargs)

    async def delete_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.DELETE_CUSTOMER, **kwargs)

    async def get_customer_detail(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMER_BY_ID, **kwargs)
  
    async def get_customer_list(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_ALL_CUSTOMER, **kwargs)
