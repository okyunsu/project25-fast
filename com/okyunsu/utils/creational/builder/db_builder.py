import asyncpg
import os
from dotenv import load_dotenv
from com.okyunsu.utils.creational.builder.query_builder import QueryBuilder
from com.okyunsu.utils.creational.singleton import db_singleton
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Async Database Builder
class DatabaseBuilder:
    def __init__(self):
        if not hasattr(db_singleton, "db_url"):
            raise AttributeError("⚠️ db_singleton 인스턴스에 'db_url' 속성이 존재하지 않습니다.")
        
        print(f"✅ Initializing DatabaseBuilder... db_url: {db_singleton.db_url}")  # 디버깅

        self.database_url = db_singleton.db_url
        self.min_size = 1
        self.max_size = 10
        self.timeout = 60
        self.pool = None



    def pool_size(self, min_size: int = 1, max_size: int = 10):
        self.min_size = min_size
        self.max_size = max_size
        return self

    def timeout(self, timeout: int = 60):
        self.timeout = timeout
        return self

    async def build(self):
        if not self.database_url:
            raise ValueError("⚠️ Database URL must be set before building the database")

        print(f"🚀 Connecting to PostgreSQL: {self.database_url}")  # 디버깅

        self.pool = await asyncpg.create_pool(
            dsn=self.database_url,
            min_size=self.min_size,
            max_size=self.max_size,
            timeout=self.timeout,
        )
        return AsyncDatabase(self.pool)

# Async Database Wrapper
class AsyncDatabase:
    def __init__(self, pool):
        self.pool = pool
        self.pending_entities = []  # 임시 저장소

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def close(self):
        await self.pool.close()
        
    # SQLAlchemy 스타일 메서드 구현 (ORM처럼 동작)
    def add(self, entity):
        """ORM 스타일로 엔티티 추가"""
        print(f"✅ 엔티티 추가: {entity}")
        self.pending_entities.append(entity)
        return self
        
    async def commit(self):
        """변경사항 커밋"""
        print(f"✅ 커밋 시작 (대기 엔티티: {len(self.pending_entities)}개)")
        try:
            for entity in self.pending_entities:
                # Customer 엔티티인 경우
                if hasattr(entity, 'user_id') and hasattr(entity, 'email'):
                    query = """
                    INSERT INTO users (user_id, name, email, password)
                    VALUES ($1, $2, $3, $4)
                    RETURNING *
                    """
                    await self.execute(
                        query,
                        entity.user_id,
                        entity.name,
                        entity.email,
                        entity.password
                    )
                    print(f"✅ 엔티티 저장 완료: {entity.user_id}")
            
            # 커밋 완료 후 목록 초기화
            self.pending_entities = []
            print("✅ 커밋 완료")
            return True
        except Exception as e:
            print(f"❌ 커밋 실패: {str(e)}")
            await self.rollback()
            raise e
            
    async def rollback(self):
        """변경사항 롤백"""
        print("✅ 롤백 수행")
        self.pending_entities = []
        return self
        
    async def refresh(self, entity):
        """엔티티 새로고침 (최신 정보 가져오기)"""
        print(f"✅ 엔티티 새로고침: {entity}")
        if hasattr(entity, 'user_id'):
            query = "SELECT * FROM users WHERE user_id = $1"
            result = await self.fetch(query, entity.user_id)
            if result and len(result) > 0:
                record = dict(result[0])
                for key, value in record.items():
                    setattr(entity, key, value)
        return entity



async def get_db():
    # .env 파일 강제 로드
    load_dotenv()

    # if not hasattr(db_singleton, "db_url") or not db_singleton.db_url:
    #     print("⚠️ db_singleton이 올바르게 초기화되지 않았습니다. 환경 변수를 다시 로드합니다.")
    #     db_singleton.db_url = os.getenv("DB_URL")
        
    #     if not db_singleton.db_url:
    #         raise AttributeError("❌ 환경 변수를 다시 로드했지만 'db_url'이 설정되지 않았습니다. .env 파일을 확인하세요.")

    # print(f"✅ db_singleton 초기화 확인: {db_singleton.db_url}")  # Debug 로그

    # PostgreSQL URL을 asyncpg 형식으로 변환
    if db_singleton.db_url.startswith('postgresql://'):
        db_singleton.db_url = db_singleton.db_url.replace('postgresql://', 'postgresql+asyncpg://')

    if not hasattr(db_singleton, 'engine'):
        db_singleton.engine = create_async_engine(
            db_singleton.db_url,
            echo=True,
            future=True
        )
        db_singleton.async_session = sessionmaker(
            db_singleton.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async with db_singleton.async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


# ✅ 4. 초기화 함수 (비동기 DB 테이블 생성)
async def init_db():
    """데이터베이스 초기화"""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


# ✅ 5. 사용 예시
if __name__ == "__main__":
    # 🔹 SQLAlchemy DB 설정 빌드
    db_builder = (
        DatabaseBuilder()
        .echo(True)
        .future(True)
        .build()
    )

    engine = db_builder._engine
    session_local = db_builder._session_local
    Base = db_builder._base

    # 🔹 pymysql 쿼리 실행 예시
    query_result = (
        QueryBuilder()
        .connect()
        .query("SELECT * FROM users")
        .execute()
    )
    
    print(f"Query Result: {query_result}")