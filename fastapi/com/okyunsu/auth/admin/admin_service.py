class AdminService:
    def __init__(self):
        pass

 
    def add_admin(self, admin):
        print(f"➕사용자 추가: {admin}")
        return admin

    def get_admin(self, admin):
        print(f"👀사용자 조회: {admin}")

        return admin

    def update_admin(self, admin):
        print(f"🔮사용자 수정: {admin}")

        return admin

    def delete_admin(self, admin):
        print(f"➖사용자 삭제: {admin}")

        return "Success"
 
    