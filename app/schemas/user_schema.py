from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.user import UserStatus
from app.schemas.common_schema import FullName, Mobile, Password, Username

class UserCreate(BaseModel):
    username: Username
    email: EmailStr
    password: Password
    full_name: FullName | None = None  # Optional
    mobile: Mobile | None = None
    
class UserUpdate(BaseModel):
    username: Username | None = None
    email: EmailStr | None = None
    full_name: FullName | None = None
    mobile: Mobile | None = None
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None 
    mobile: str | None = None
    status: UserStatus
    email_verified: bool
    last_loin_at: datetime | None = None
    password_changed_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
    