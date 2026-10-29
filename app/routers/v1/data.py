from fastapi import APIRouter, status, Depends
from app.schemas import URLResponse, URLCreate
from app.services import shortener
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/v1", tags=["Data"])


@router.post("/data/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def shorten(url: URLCreate, db:Session = Depends(get_db)):
    long_url = str(url.long_url)
    code = shortener.create_short_url(long_url, db)
    return URLResponse(short_url=code, long_url=long_url)
