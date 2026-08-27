from pydantic import BaseModel, EmailStr

from app.schemas.common_schema import Password

class LoginRequest(BaseModel):
    email: EmailStr
    password: Password
    
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"