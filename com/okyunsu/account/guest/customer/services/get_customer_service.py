from com.okyunsu.account.guest.customer.storages.get_customer import get_all_customer, get_customer_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService


class GetAllCustomer(AbstractService):

    async def handle(self, **kwargs):
        db = kwargs.get("db")
        try:
            # AsyncDatabase 객체는 begin 메서드가 없으므로 직접 호출
            customers = await get_all_customer(db)
            
            # 딕셔너리를 리스트로 변환 (응답 모델과 일치시키기 위해)
            if isinstance(customers, dict):
                # 오류 응답인 경우 처리
                if "error" in customers:
                    print(f"⚠️ 저장소에서 오류 반환: {customers['error']}")
                    return []
                
                # 딕셔너리 값들을 리스트로 변환
                customers_list = list(customers.values())
                print(f"🔍 딕셔너리를 리스트로 변환: {len(customers_list)}개 항목")
                return customers_list
            
            return customers  # ✅ 성공 시 데이터 반환
        except Exception as e:
            print("[ERROR] GetAllCustomer failed:", str(e))
            return []  # 빈 리스트 반환 (검증 오류 방지)

class GetCustomerById(AbstractService):

    async def handle(self, **kwargs):
        db = kwargs.get("db")
        user_id = kwargs.get("user_id")
        
        if not user_id:
            print("⚠️ user_id가 제공되지 않았습니다.")
            return {"error": "User ID is required"}
            
        try:
            customer = await get_customer_by_id(db, user_id)
            return customer
        except Exception as e:
            print(f"⚠️ 고객 상세 조회 중 오류 발생: {str(e)}")
            return {"error": f"Failed to retrieve customer: {str(e)}"}