# 1. Python 3.10 기반 Docker 이미지 사용
FROM python:3.12.7-slim

# 2. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 복사 및 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 전체 복사
COPY . /app

# 5. FastAPI 실행 (포트 8000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]