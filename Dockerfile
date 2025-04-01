# 1. Python 3.10 기반 Docker 이미지 사용
FROM python:3.12.7-slim

# 2. 비-root 사용자 생성
RUN useradd -m -u 1000 appuser

# 3. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /backend

# 4. requirements.txt 복사 및 패키지 설치
COPY requirements.txt /backend/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir asyncpg email-validator

# 5. 소스 코드 전체 복사
COPY . /backend/

# 6. 소유권 변경
RUN chown -R appuser:appuser /backend

# 7. 비-root 사용자로 전환
USER appuser

# 8. FastAPI 실행 (포트 8000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]