from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    role: str = 'student'

class UserCreate(User):
    password: str

class UserResponse(User):
    id: int
    class Config:
        orm_mode = True