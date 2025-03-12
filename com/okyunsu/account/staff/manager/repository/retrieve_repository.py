from com.okyunsu.account.staff.manager.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession

class RetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        try:
            query = "SELECT user_id, email, name FROM member"
            members = await db.fetch(query) 
            
            result = []
            for member in members:
                member_data = {
                    "user_id": member['user_id'],
                    "email": member['email'],
                    "name": member['name']
                }
                result.append(member_data)
            
            print("✅ 조회된 사용자 목록:", result)
            return result
            
        except Exception as e:
            print("❌ 데이터 조회 중 오류 발생:", str(e))
            return []
        

class DefaultRetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass
