import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

app = FastAPI()

# Izinkan Frontend mengakses API ini (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.get("/")
def home():
    return {"status": "The Reading Nook API is Online!"}

@app.get("/api/books")
def get_all_books():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books ORDER BY id DESC")
        books = cur.fetchall()
        cur.close()
        conn.close()
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/books/{book_id}")
def get_one_book(book_id: int): # FastAPI otomatis mengubah string ke integer
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Gunakan query SQL untuk mencari berdasarkan ID
        cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cur.fetchone()
        cur.close()
        conn.close()

        if book:
            return book
        else:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan di database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))