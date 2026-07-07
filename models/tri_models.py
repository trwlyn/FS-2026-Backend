from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# 1. Model untuk menerima data dari Formulir Kontak
class ContactIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str # Anda bisa gunakan EmailStr jika sudah install 'pydantic[email]'
    message: str = Field(..., min_length=5)

# 2. Model untuk menampilkan data Buku (sesuai kolom di Neon DB)
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str] = None
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    availability_status: Optional[str] = "Available"

# 3. Model untuk Respon Sukses (Opsional, agar API lebih terstruktur)
class SuccessResponse(BaseModel):
    message: str