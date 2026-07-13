import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# 1. Memuat variabel lingkungan dari file .env
load_dotenv()

# 2. Mengambil URL Database dari .env
DATABASE_URL = os.getenv("DATABASE_URL")
def get_db_connection():
    """
    Fungsi untuk membuat koneksi baru ke Neon PostgreSQL.
    Menggunakan RealDictCursor agar hasil query berupa Dictionary (JSON friendly).
    """
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"CRITICAL ERROR: Could not connect to database. {e}")
        return None