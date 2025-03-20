from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


async def get_all_customer(db):  # AsyncSession 타입 힌트 제거
    try:
        # AsyncDatabase 객체의 fetch 메서드 사용
        records = await db.fetch("SELECT * FROM users")
        
        # 리스트 대신 딕셔너리로 변환
        customers_dict = {}
        for record in records:
            # asyncpg의 Record 객체를 딕셔너리로 변환
            customer = dict(record)
            if "user_id" in customer:
                customers_dict[customer["user_id"]] = customer
            else:
                # user_id가 없는 경우 대체 키 사용
                key = customer.get("id") or str(len(customers_dict))
                customers_dict[key] = customer
            
        return customers_dict
    except Exception as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        return {"error": str(e)}  # 예외를 발생시키지 않고 오류 메시지 반환


async def get_customer_by_id(db, user_id: str):
    try:
        # 테이블 이름 결정 (users 또는 member 또는 다른 테이블)
        try:
            tables_query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
            tables_result = await db.fetch(tables_query)
            tables = [dict(r)["table_name"] for r in tables_result]
            
            table_name = "users"
            if "users" not in tables and "member" in tables:
                table_name = "member"
            elif "users" not in tables and "members" in tables:
                table_name = "members"
                
            # 실제 쿼리 실행
            query = f"SELECT * FROM {table_name} WHERE user_id = $1 OR id = $1 LIMIT 1"
            record = await db.fetch(query, user_id)
            
            if not record or len(record) == 0:
                return {"error": "Customer not found"}
                
            return dict(record[0])
        except Exception as e:
            print(f"⚠️ 테이블 조회 중 오류 발생: {str(e)}")
            # 기본 쿼리 시도
            query = "SELECT * FROM users WHERE user_id = $1 OR id = $1 LIMIT 1"
            record = await db.fetch(query, user_id)
            
            if not record or len(record) == 0:
                return {"error": "Customer not found"}
                
            return dict(record[0])
    except Exception as e:
        print(f"⚠️ 고객 조회 중 오류 발생: {str(e)}")
        return {"error": f"Failed to retrieve customer: {str(e)}"}





