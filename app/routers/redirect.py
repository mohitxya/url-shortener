from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from app.services import shortener
from app.services.errors import InvalidShortCode, ShortCodeNotFound

router = APIRouter(tags=["Redirect"])


@router.get("/{short_code}")
def redirect(short_code: str):
    try:
        long_url = shortener.get_long_url(short_code)
    except (InvalidShortCode, ShortCodeNotFound):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
    return RedirectResponse(url=long_url, status_code=302)