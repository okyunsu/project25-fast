


from com.okyunsu.auth import HelloScore


strategy_map = {
    "hello_user": HelloScore(),
}

class ScoreFactory:
    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)    