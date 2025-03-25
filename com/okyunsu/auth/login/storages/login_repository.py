from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from com.okyunsu.auth.login.models.login_schema import LoginRequest

class LoginRepository:
    async def verify_login(self, db: AsyncSession, login_data: LoginRequest):
        try:
            query = text("""
                SELECT user_id, name 
                FROM users 
                WHERE user_id = :user_id AND password = :password
            """)
            
            result = await db.execute(
                query,
                {
                    "user_id": login_data.user_id,
                    "password": login_data.password
                }
            )
            
            user = result.first()
            if not user:
                return None
                
            return {
                "user_id": user.user_id,
                "name": user.name
            }
            
        except Exception as e:
            print(f"[ERROR] Login verification failed: {e}")
            return None 