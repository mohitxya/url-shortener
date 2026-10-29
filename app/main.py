from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router as api_router
import time


app = FastAPI(title="URL Shortener API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    # Pass the request down to the actual route handler:
    response = await call_next(request)
    # Calculate how long the route took in seconds:
    process_time = time.perf_counter() - start_time
    # Convert seconds to milliseconds (ms) with 2 decimal places and attach to headers:
    response.headers["X-Process-Time"] = f"{process_time * 1000:.2f}ms"
    return response

@app.get("/")
def read_root():
    return {"message": "URL Shortener API"}


app.include_router(api_router)