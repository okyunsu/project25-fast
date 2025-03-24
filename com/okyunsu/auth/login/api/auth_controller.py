from com.okyunsu.auth.login.models.login_action import LoginAction
from com.okyunsu.auth.login.api.auth_factory import AuthFactory

class AuthController:
    async def login(self, **kwargs):
        return await AuthFactory.create(
            strategy=LoginAction.LOGIN,
            **kwargs
        )

    async def logout(self, **kwargs):
        return await AuthFactory.create(
            strategy=LoginAction.LOGOUT,
            **kwargs
        ) 