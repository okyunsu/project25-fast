from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService

class DefaultDeleteRepository(AbstractService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        try:
            print(f"🔍 삭제 시도: user_id = {user_id}")
            # users 테이블에서 user_id에 해당하는 사용자 삭제
            query = text("DELETE FROM users WHERE user_id = :user_id")
            result = await db.execute(query, {"user_id": user_id})
            await db.commit()
            
            print(f"🗑️ 사용자 삭제 완료: {user_id}")
            return True
            
        except Exception as e:
            print(f"[ERROR] 사용자 삭제 실패: {e}")
            await db.rollback()
            return False

class ValidDeleteRepository(AbstractService):
    async def delete(self, db: AsyncSession, user_id: str, new_customer: CustomerSchema):
        try:
            print(f"🔍 삭제 검증 시도: user_id = {user_id}")
            # 삭제 전에 사용자가 존재하는지 확인
            check_query = text("SELECT user_id FROM users WHERE user_id = :user_id")
            result = await db.execute(check_query, {"user_id": user_id})
            user = result.scalar()
            
            if not user:
                print(f"⚠️ 사용자를 찾을 수 없음: {user_id}")
                return False
                
            # 사용자 삭제
            delete_query = text("DELETE FROM users WHERE user_id = :user_id")
            await db.execute(delete_query, {"user_id": user_id})
            await db.commit()
            
            print(f"✅ 사용자 삭제 완료: {user_id}")
            return True
            
        except Exception as e:
            print(f"[ERROR] 사용자 삭제 실패: {e}")
            await db.rollback()
            return False
