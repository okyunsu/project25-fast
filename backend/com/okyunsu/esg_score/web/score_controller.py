

from com.okyunsu.esg_score.web.score_factory import ScoreFactory


class ScoreController:
    def __init__(self):
        pass

    def hello_user(self,**kwargs):
        return ScoreFactory.create(strategy="hello_user",**kwargs)  