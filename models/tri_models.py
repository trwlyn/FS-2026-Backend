from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# 1. Model for receiving data from Contact Form
class ContactIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str #
    message: str = Field(..., min_length=5)

# 2.Model for displaying Book data (according to columns in Neon DB)
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str] = None
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    availability_status: Optional[str] = "Available"

# 3. Model for success response
class SuccessResponse(BaseModel):
    message: str