import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.tri_endpoints import router as tri_endpoints

# Load variabel from file .env
load_dotenv()

docs_url =os.getenv("DOCS_URL","/docs")
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app = FastAPI(docs_url=docs_url)

# Allowed Frontend to access API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tri_endpoints)

@app.get("/")
def home():
    return {"status": "The Reading Nook API is Online!"}

