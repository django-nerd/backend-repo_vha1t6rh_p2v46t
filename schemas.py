from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contact(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., description="Message body")
    source: Optional[str] = Field("portfolio", description="Where the lead came from")
