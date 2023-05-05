from typing import Optional, List

from pydantic import BaseModel, EmailStr
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

class UserSignIn(BaseModel):
    email: EmailStr
    password: str