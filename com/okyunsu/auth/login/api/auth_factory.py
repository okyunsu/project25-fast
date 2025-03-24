from com.okyunsu.auth.login.models.login_action import LoginAction
from com.okyunsu.auth.login.services.login_service import LoginService

class AuthFactory:
    strategy_map = {
        LoginAction.LOGIN: LoginService(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = AuthFactory.strategy_map.get(strategy)
        if not instance:
            raise Exception("Invalid auth strategy")
        return await instance.handle(**kwargs) 