from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.account.guest.customer.storages.create_customer_command import create_customer

class CreateCustomer(AbstractService):
    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        schema: CustomerSchema = kwargs.get("customer")  
        
        if not schema:
            print("⚠️ customer 데이터가 None입니다.")
            return {"error": "Customer data is required"}
            
        try:
            # 엔티티 생성
            customer = await create_customer(schema)
            
            # SQLAlchemy ORM을 사용하여 데이터베이스에 저장
            query = text("""
                INSERT INTO users (user_id, name, email, password)
                VALUES (:user_id, :name, :email, :password)
                RETURNING *
            """)
            
            result = await db.execute(
                query,
                {
                    "user_id": customer.user_id,
                    "name": customer.name,
                    "email": customer.email,
                    "password": customer.password
                }
            )
            
            # commit은 get_db에서 처리됨
            
            return {
                "user_id": customer.user_id,
                "name": customer.name,
                "email": customer.email,
                "password": customer.password,
                "message": "Customer created successfully"
            }
        except Exception as e:
            print(f"[ERROR] CustomerCreate failed: {e}")
            # rollback은 get_db에서 처리됨
            return {"error": str(e)}






