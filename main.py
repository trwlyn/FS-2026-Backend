import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.tri_endpoints import router as tri_endpoints

# Load variabel dari file .env

app = FastAPI()

# Izinkan Frontend mengakses API ini (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tri_endpoints)

@app.get("/")
def home():
    return {"status": "The Reading Nook API is Online!"}

