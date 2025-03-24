from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


async def get_all_customer(db: AsyncSession):
    try:
        # SQLAlchemy text()를 사용한 쿼리 실행
        query = text("SELECT * FROM users")
        result = await db.execute(query)
        records = result.fetchall()
        
        # 리스트 대신 딕셔너리로 변환
        customers_dict = {}
        for record in records:
            # Row 객체를 딕셔너리로 변환
            customer = dict(zip(record.keys(), record))
            if "user_id" in customer:
                customers_dict[customer["user_id"]] = customer
            else:
                # user_id가 없는 경우 대체 키 사용
                key = customer.get("id") or str(len(customers_dict))
                customers_dict[key] = customer
            
        return customers_dict
    except Exception as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        return {"error": str(e)}


async def get_customer_by_id(db: AsyncSession, user_id: str):
    try:
        # 테이블 이름 결정 (users 또는 member 또는 다른 테이블)
        tables_query = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables_result = await db.execute(tables_query)
        tables = [row[0] for row in tables_result.fetchall()]
        
        table_name = "users"
        if "users" not in tables and "member" in tables:
            table_name = "member"
        elif "users" not in tables and "members" in tables:
            table_name = "members"
            
        # 실제 쿼리 실행
        query = text(f"SELECT * FROM {table_name} WHERE user_id = :user_id OR id = :user_id LIMIT 1")
        result = await db.execute(query, {"user_id": user_id})
        record = result.first()
        
        if not record:
            return {"error": "Customer not found"}
            
        # Row 객체를 딕셔너리로 변환
        return dict(zip(record.keys(), record))
        
    except Exception as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        return {"error": str(e)}





