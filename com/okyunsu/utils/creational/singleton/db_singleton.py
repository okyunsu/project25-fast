import os
from threading import Lock
from dotenv import load_dotenv


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../"))
load_dotenv(os.path.join(project_root, ".env"))

class DataBaseSingleton():
    
    _instance = None
    _lock = Lock()  # :white_check_mark: 멀티스레드 환경에서도 안전하게 인스턴스를 생성하도록 락 사용

    def __new__(cls):
        
        if not cls._instance:
            with cls._lock:  # :white_check_mark: 멀티스레드 환경에서 안전하게 인스턴스 생성
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """환경 변수 값을 로드하여 설정 초기화"""

        is_docker = os.path.exists('/.dockerenv') or os.environ.get('DOCKER_CONTAINER') == 'true'

        self.db_username = os.getenv("DB_USERNAME")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_port = int(os.getenv("DB_PORT", 5432))
        self.db_database = os.getenv("DB_DATABASE")
        self.db_charset = os.getenv("DB_CHARSET", "utf8mb4")

        # Docker 환경에서는 서비스 이름을 사용, 로컬에서는 localhost 사용
        if is_docker:
            self.db_hostname = os.getenv("DB_HOSTNAME", "db")
        else:
            self.db_hostname = os.getenv("DB_HOSTNAME", "localhost")


        # ✅ 환경 변수 검증
        # if None in (self.db_username, self.db_password, self.db_database):
        #     raise ValueError("⚠️ Database 환경 변수가 설정되지 않았습니다.")

        # ✅ PostgreSQL에 맞는 URL 형식
        self.db_url = f"postgresql://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"
        print(f"✅ Database URL: {self.db_url}")  # 디버깅 출력SE: {self.db_database}")

db_singleton = DataBaseSingleton()
print("💦💫♾️📛", db_singleton.db_url)

    