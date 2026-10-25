from fastapi import FastAPI
import routers as app_routers
from threading import Lock


urls: dict[int, str] = {}
reverse: dict[str, int] = {}

_counter = 0
_lock = Lock()


app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "URL Shortener API"}

app.include_router(app_routers.router)