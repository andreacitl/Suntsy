from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class UserRegister(BaseModel):
    email: EmailStr
    password: str 
    name: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str