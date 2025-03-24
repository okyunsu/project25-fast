from sqlalchemy.ext.asyncio import AsyncSession
from com.okyunsu.account.guest.customer.models.customer_schema import CustomerSchema
from com.okyunsu.utils.creational.abstract.abstract_service import AbstractService
from com.okyunsu.account.guest.customer.storages.delete_repository import DefaultDeleteRepository, ValidDeleteRepository

class DeleteCustomer(AbstractService): 
    async def handle(self, **kwargs):
        try:
            db = kwargs.get("db")
            user_id = kwargs.get("user_id")
            print("🔍🔍 db 정보:", db)
            
            if not user_id:
                return {"success": False, "message": "사용자 ID가 필요합니다."}
            
            repository = DefaultDeleteRepository()
            result = await repository.delete(db, user_id, None)
            
            if result:
                return {
                    "success": True,
                    "message": f"사용자 {user_id}가 성공적으로 삭제되었습니다."
                }
            else:
                return {
                    "success": False,
                    "message": "사용자 삭제 중 오류가 발생했습니다."
                }
                
        except Exception as e:
            print(f"[ERROR] DeleteCustomer failed: {e}")
            return {"success": False, "message": str(e)}

class RemoveCustomer(AbstractService):
    async def handle(self, **kwargs):
        try:
            db = kwargs.get("db")
            user_id = kwargs.get("user_id")
            
            if not user_id:
                return {"success": False, "message": "사용자 ID가 필요합니다."}
            
            repository = ValidDeleteRepository()
            result = await repository.delete(db, user_id, None)
            
            if result:
                return {
                    "success": True,
                    "message": f"사용자 {user_id}가 검증 후 삭제되었습니다."
                }
            else:
                return {
                    "success": False,
                    "message": "사용자가 존재하지 않거나 삭제할 수 없습니다."
                }
                
        except Exception as e:
            print(f"[ERROR] RemoveCustomer failed: {e}")
            return {"success": False, "message": str(e)}