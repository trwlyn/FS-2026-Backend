# 1. Gunakan image Python resmi yang ringan
FROM python:3.9-slim

# 2. Set folder kerja di dalam container
WORKDIR /app

# 3. Instal dependencies sistem untuk psycopg2 (koneksi database)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Salin file requirements.txt terlebih dahulu agar proses build lebih cepat (caching)
COPY requirements.txt .

# 5. Instal library Python yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# 6. Salin semua kode backend Anda ke dalam container
COPY . .

# 7. Expose port 8000 (port default FastAPI)
EXPOSE 8000

# 8. Jalankan perintah untuk memulai server FastAPI
# Kita gunakan 0.0.0.0 agar bisa diakses dari luar container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]