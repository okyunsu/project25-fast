from com.okyunsu.account.common.user.model.user_schema import UserSchema
from pydantic import BaseModel




class LoginRequest(BaseModel):
    user_id: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    message: str
    token: str | None = None
    user_id: str | None = None
    name: str | None = None

