from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str
    role: str = "user"
    is_active: bool
    created_at: 

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"