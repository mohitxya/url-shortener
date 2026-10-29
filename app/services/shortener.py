import string
from app.services.errors import InvalidShortCode, ShortCodeNotFound
from sqlalchemy.orm import Session
from app.models import URL
from app.database import r, SessionLocal
from app.config import settings


BASE62 = string.ascii_letters + string.digits
BASE = len(BASE62) # gives 62 distinct characters: 26 + 26 + 10 = 62.




def encode(num: int) -> str:
    if num == 0:
        return BASE62[0]
    chars = []
    while num > 0:
        chars.append(BASE62[num % BASE])
        num //= BASE
    return "".join(reversed(chars))


def decode(code: str) -> int:
    num = 0
    for char in code:
        idx = BASE62.find(char)
        if idx == -1:
            raise InvalidShortCode(f"Invalid character in short code: {char}")
        num = num * BASE + idx
    return num


def create_short_url(long_url: str, db:Session) -> str:
    existing = db.query(URL).filter(URL.original_url == long_url).first()
    if existing: 
        return existing.short_url
    
    # too slow: count = db.query(URL).count()
    new_url = URL(
        original_url=long_url,
    ) 
    db.add(new_url)
    db.flush() # assign id without commit
    new_url.short_url = encode(new_url.id)
    db.commit()
    return new_url.short_url
        


def get_long_url(short_code: str) -> str: #, db:Session
    cached_url = r.get(short_code)
    if cached_url: 
        return cached_url
    url_id = decode(short_code)

    with SessionLocal() as db:
        url_record = db.query(URL).filter(URL.id == url_id).first()
        if not url_record:
            raise ShortCodeNotFound(f"Short code {short_code} not found")
            
    r.setex(short_code, settings.redis_ttl_seconds, url_record.original_url)
    return url_record.original_url
