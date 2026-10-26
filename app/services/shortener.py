import string
from threading import Lock
from app.services.errors import InvalidShortCode, ShortCodeNotFound

BASE62 = string.ascii_letters + string.digits
BASE = len(BASE62) # gives 62 distinct characters: 26 + 26 + 10 = 62.

_counter = 100000
_lock = Lock()


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


def create_short_url(long_url: str) -> str:
    global _counter
    with _lock:
        if long_url in _url_to_id:
            return encode(_url_to_id[long_url])
        # if not in database
        _counter += 1
        url_id = _counter
        _id_to_url[url_id] = long_url
        _url_to_id[long_url] = url_id
        return encode(url_id)


def get_long_url(short_code: str) -> str:
    url_id = decode(short_code)
    with _lock:
        if url_id not in _id_to_url:
            raise ShortCodeNotFound(f"Short code {short_code} not found")
        return _id_to_url[url_id]
