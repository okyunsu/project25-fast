from com.okyunsu.account.leadership.director.strategy.strategy_type import StrategyType
from com.okyunsu.account.leadership.director.strategy.create_strategy import DefaultCreateStrategy, ValidCreateStrategy
from com.okyunsu.account.leadership.director.strategy.delete_strategy import  SoftDeleteStrategy, HardDeleteStrategy
from com.okyunsu.account.leadership.director.strategy.retrieve_strategy import GetAllStrategy, GetDetailStrategy
from com.okyunsu.account.leadership.director.strategy.update_strategy import FullUpdateStrategy, PartialUpdateStrategy
from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession

class DirectorFactory():


    strategy_map = {
        StrategyType.DEFAULT_CREATE: DefaultCreateStrategy(),
        StrategyType.VALID_CREATE: ValidCreateStrategy(),
        StrategyType.SOFT_DELETE: SoftDeleteStrategy(),
        StrategyType.HARD_DELETE: HardDeleteStrategy(),
        StrategyType.GET_ALL: GetAllStrategy(),
        StrategyType.GET_DETAIL: GetDetailStrategy(),
        StrategyType.FULL_UPDATE: FullUpdateStrategy(),
        StrategyType.PARTIAL_UPDATE: PartialUpdateStrategy(),
    }

    @staticmethod
    async def execute(
        strategy: StrategyType, 
        method: Literal["create", "retrieve", "update", "delete"], 
        db: AsyncSession,
        **kwargs
    ):
        instance = DirectorFactory.strategy_map.get(strategy)
        if not instance:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        if not hasattr(instance, method):
            raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

        method_to_call = getattr(instance, method)

        # 비동기 메서드 여부 확인 후 실행
        if callable(method_to_call):
            if method == "retrieve":  
                return await method_to_call(db=db, **kwargs)
            else:
                return await method_to_call(db=db, **kwargs)
        else:
            raise TypeError(f"Method '{method}' is not callable.")