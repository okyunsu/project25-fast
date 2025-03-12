
from fastapi import APIRouter

from com.okyunsu.esg_score.web.score_controller import ScoreController


router = APIRouter()
controller = ScoreController()

@router.get(path='/')
async def home_score():
    return controller.hello_score()


