from pydantic import BaseModel, EmailStr, Field

# ✅ 공통 User 스키마 (상속용)
class UserSchema(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: str = Field(..., min_length=4, max_length=50)

    class Config:
        orm_mode = True  # SQLAlchemy 객체를 자동 변환 가능

# # ✅ 입력용 User 스키마 (회원가입, 로그인 시 사용)
# class UserSchemaIn(UserBase):
#     password: str = Field(..., min_length=8, max_length=50)

# # ✅ 출력용 User 스키마 (API 응답에서 password 제외)
# class UserSchemaOut(UserBase):
#     pass  # 추가 필드 없이 상속만 활용 (password 자동 제외)
