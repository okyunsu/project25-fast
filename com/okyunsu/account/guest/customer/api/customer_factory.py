from typing import Literal
from com.okyunsu.account.guest.customer.services.create_customer_service import CreateCustomer
from com.okyunsu.account.guest.customer.services.delete_customer_sevice import RemoveCustomer, DeleteCustomer
from com.okyunsu.account.guest.customer.services.get_customer_service import GetAllCustomer, GetCustomerById
from com.okyunsu.account.guest.customer.services.find_customer_service import FindCustomers
from com.okyunsu.account.guest.customer.services.update_customer_service import UpdateCustomer, PartialUpdateCustomer
from com.okyunsu.account.guest.customer.models.customer_action import CustomerAction


class CustomerFactory:

    strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
        CustomerAction.REMOVE_CUSTOMER: RemoveCustomer(),
        CustomerAction.FIND_CUSTOMER: FindCustomers(),
        CustomerAction.GET_ALL_CUSTOMER: GetAllCustomer(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetCustomerById(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.PATCH_CUSTOMER: PartialUpdateCustomer(),
        
    }


    @staticmethod
    async def create(strategy, **kwargs):
        instance = CustomerFactory.strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)


    # @staticmethod
    # async def execute(strategy: CustomerAction, method: Literal["create","retrieve","update","delete"],**kwargs):
    #     instance = CustomerFactory.strategy_map[strategy]
    #     if not instance:
    #         raise ValueError(f"Invalid strategy: {strategy}")
        
    #     if not hasattr(instance, method):
    #         raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

    #     method_to_call = getattr(instance, method)
    #     return await method_to_call(**kwargs)  # 동적으로 해당 메서드를 실행


