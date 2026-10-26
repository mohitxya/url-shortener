from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router as api_router

app = FastAPI(title="URL Shortener API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "URL Shortener API"}


app.include_router(api_router)