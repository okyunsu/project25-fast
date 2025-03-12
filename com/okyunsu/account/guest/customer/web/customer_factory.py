


from typing import Literal
from com.okyunsu.account.guest.customer.strategy.create_strategy import DefaultCreateStrategy, ValidCreateStrategy
from com.okyunsu.account.guest.customer.strategy.delete_strategy import HardDeleteStrategy, SoftDeleteStrategy
from com.okyunsu.account.guest.customer.strategy.retrieve_strategy import GetAllStrategy, GetDetailStrategy
from com.okyunsu.account.guest.customer.strategy.strategy_type import StrategyType
from com.okyunsu.account.guest.customer.strategy.update_strategy import FullUpdateStrategy, PartialUpdateStrategy



class CustomerFactory:

    strategy_map = {
        StrategyType.DEFAULT_CREATE: DefaultCreateStrategy(),
        StrategyType.VALIDATED_CREATE: ValidCreateStrategy(),
        StrategyType.GET_ALL: GetAllStrategy(),
        StrategyType.GET_DETAIL: GetDetailStrategy(),
        StrategyType.FULL_UPDATE: FullUpdateStrategy(),
        StrategyType.PARTIAL_UPDATE: PartialUpdateStrategy(),
        StrategyType.SOFT_DELETE: SoftDeleteStrategy(),
        StrategyType.HARD_DELETE: HardDeleteStrategy(),
    }


    @staticmethod
    async def execute(strategy: StrategyType, method: Literal["create","retrieve","update","delete"],**kwargs):
        instance = CustomerFactory.strategy_map[strategy]
        if not instance:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        if not hasattr(instance, method):
            raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

        method_to_call = getattr(instance, method)
        return await method_to_call(**kwargs)  # 동적으로 해당 메서드를 실행


