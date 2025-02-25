class UserService:
    def __init__(self):
        pass

    
    def add_user(self, user):
        print(f"➕사용자 추가: {user}")
        return user

    def get_user(self, user):
        print(f"👀사용자 조회: {user}")

        return user

    def update_user(self, user):
        print(f"🔮사용자 수정: {user}")

        return user

    def delete_user(self, user):
        print(f"➖사용자 삭제: {user}")

        return "Success"
 
    