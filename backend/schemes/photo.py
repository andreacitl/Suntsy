from pydantic import BaseModel, Field
from typing import Optional

class Photo(BaseModel):
    user_id: str
    day: str
    caption: Optional[str] = None
    location: Optional[str] = None
    
    
class UpdatePhoto(BaseModel):
    user_id: str 
    day: str
    caption: Optional[str] = None
    location: Optional[str] = None
