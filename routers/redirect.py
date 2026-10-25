from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from services import shortener
from services.errors import InvalidShortCode, ShortCodeNotFound

router = APIRouter()

@router.get('/{short_code}')
def redirect(short_code: str):
    try: 
        long_url = shortener.get_long_url(short_code)
    except InvalidShortCode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Short URL not found')
    return RedirectResponse(url=long_url, status_code=302)