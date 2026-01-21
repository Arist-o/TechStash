from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

# 1. Додаємо перелік доступних ролей
class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"

class UserBase(BaseModel):
    email: EmailStr
    username: str
    role: Role = Role.USER # Додаємо роль у базову модель із замовчуванням "user"

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: str = Field(alias="_id")

    class Config:
        populate_by_name = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None # Додаємо можливість змінити роль через PATCH

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"