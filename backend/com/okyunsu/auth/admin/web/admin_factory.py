
from com.okyunsu.auth.admin.service.hello_admin import HelloAdmin


strategy_map = {
    "hello_user": HelloAdmin(),
}

class AdminFactory:
    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)    