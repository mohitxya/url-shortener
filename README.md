# url-shortener
A URL shortener built with FastAPI, using base-62 encoding, with caching, rate limiting, and sharding.

## Running Locally

To run the application using `uv`:

```bash
uv run python main.py
```

Or using FastAPI CLI directly:

```bash
uv run fastapi dev app/main.py
```

## API Endpoints

- `GET /`: Health check / welcome message
- `POST /api/v1/data/shorten`: Shorten a URL (JSON body: `{"long_url": "https://example.com"}`)
- `GET /{short_code}`: Redirect to the original URL
