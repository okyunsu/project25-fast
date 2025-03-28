from datetime import datetime, timezone
from typing import Callable
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pytz import timezone
from com.okyunsu.app_router import router as app_router
from fastapi.middleware.cors import CORSMiddleware
from com.okyunsu.auth.auth_router import router as auth_router
# python -m uvicorn main:app --reload   faskapi 실행
# http://127.0.0.1:8000/


load_dotenv()

app = FastAPI()
app.include_router(app_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


current_time: Callable[[], str] = lambda: datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
@app.get(path="/")
async def home():
    
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")






