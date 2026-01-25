from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Photo(BaseModel):
    user_id: str
    day: date
    caption: Optional[str] = None
    location: Optional[str] = None
    
    
class UpdatePhoto(BaseModel):
    user_id: str 
    caption: Optional[str] = None
    location: Optional[str] = None
