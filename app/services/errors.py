class InvalidShortCode(Exception):
    """Raised when a short code contains invalid characters."""
    pass


class ShortCodeNotFound(Exception):
    """Raised when a short code is not found in the database/store."""
    pass
