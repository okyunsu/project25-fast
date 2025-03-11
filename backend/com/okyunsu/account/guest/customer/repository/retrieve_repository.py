from com.okyunsu.account.common.user.model.user_entity import UserEntity
from com.okyunsu.account.guest.customer.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession

class RetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):  # async 추가
        try:
            # raw SQL 쿼리 사용
            query = "SELECT user_id, email, name FROM users"
            users = await db.fetch(query)  # AsyncDatabase의 fetch 메서드 사용
            
            # 조회된 데이터를 딕셔너리 리스트로 변환
            result = []
            for user in users:
                user_data = {
                    "user_id": user['user_id'],
                    "email": user['email'],
                    "name": user['name']
                }
                result.append(user_data)
            
            print("✅ 조회된 사용자 목록:", result)
            return result
            
        except Exception as e:
            print("❌ 데이터 조회 중 오류 발생:", str(e))
            return []
        

class DefaultRetrieveRepository(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        pass





