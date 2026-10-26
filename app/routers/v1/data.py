from fastapi import APIRouter, status
from app.schemas import URLResponse, URLCreate
from app.services import shortener

router = APIRouter(prefix="/api/v1", tags=["Data"])


@router.post("/data/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def shorten(url: URLCreate):
    long_url = str(url.long_url)
    code = shortener.create_short_url(long_url)
    return URLResponse(short_url=code, long_url=long_url)
