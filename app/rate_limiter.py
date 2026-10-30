from fastapi import Request, HTTPException, status
from app.database import r


def rate_limiter(limit: int = 5, window: int = 60):
    def dependency(request: Request):
        client_ip = request.client.host if request.client else "127.0.0.1"
        key = f"rate_limit:{client_ip}:shorten"

        pipe=r.pipeline()
        pipe.incr(key)
        pipe.ttl(key)
        current_count, time_to_live=pipe.execute()

        if current_count == 1 or time_to_live == -1:
            r.expire(key, window)
            time_to_live = window

        if current_count > limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later.",
                headers={"Retry-After": str(time_to_live)}
            )
    return dependency