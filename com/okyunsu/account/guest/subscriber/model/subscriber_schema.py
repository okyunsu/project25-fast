from pydantic import BaseModel
from typing import Optional

class SubscriberSchema(BaseModel):
    id: Optional[int] = None
    user_id: str
    name: str
    email: str
    phone: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True  # Pydantic V2에서는 orm_mode 대신 from_attributes 사용