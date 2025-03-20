from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.account.guest.customer.storges.create_customer_command import create_customer

class CreateCustomer(AbstractService):
    async def handle(self, **kwargs):
        db = kwargs.get("db")
        schema = kwargs.get("customer")  
        
        if not schema:
            print("⚠️ customer 데이터가 None입니다.")
            return {"error": "Customer data is required"}
            
        try:
            customer = await create_customer(schema)
            db.add(customer)
            await db.commit()
            await db.refresh(customer)
            
            return {
                "user_id": customer.user_id,
                "name": customer.name,
                "email": customer.email,
                "password": customer.password,
                "message": "Customer created successfully"
            }
        except Exception as e:
            print(f"[ERROR] CustomerCreate failed: {e}")
            await db.rollback()
            return {"error": str(e)}






