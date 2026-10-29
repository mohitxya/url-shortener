from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from app.services import shortener
from app.services.errors import InvalidShortCode, ShortCodeNotFound
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(tags=["Redirect"])


@router.get("/{short_code}")
def redirect(short_code: str, db:Session = Depends(get_db)):
    try:
        long_url = shortener.get_long_url(short_code, db)
    except (InvalidShortCode, ShortCodeNotFound):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
    return RedirectResponse(url=long_url, status_code=302)