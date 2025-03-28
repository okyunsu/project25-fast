from com.okyunsu.account.common.user.model.user_schema import UserSchema
from pydantic import BaseModel




class LoginRequest(BaseModel):
    user_id: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    message: str
    user_id: str | None = None
    name: str | None = None
    access_token: str | None = None
    refresh_token: str | None = None

