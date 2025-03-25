from sqlalchemy import text
from com.okyunsu.auth.login.models.login_schema import LoginRequest

def get_login_query(login_data: LoginRequest):
    return text("""
        SELECT user_id, name 
        FROM users 
        WHERE user_id = :user_id AND password = :password
    """), {
        "user_id": login_data.user_id,
        "password": login_data.password
    }

def get_user_query(user_id: str):
    return text("""
        SELECT user_id, name 
        FROM users 
        WHERE user_id = :user_id
    """), {
        "user_id": user_id
    } 