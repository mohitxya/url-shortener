from fastapi import APIRouter, status
from schemas import URLResponse, URLCreate
from services import shortener

router = APIRouter(prefix='/api/v1')

@router.post('/data/shorten', response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def shorten(url: URLCreate):
    long_url = str(url.long_url)
    code = shortener.create_short_url(long_url)

@router.get('/{short_url}')
def redirect():
    pass

