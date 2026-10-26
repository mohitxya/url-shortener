from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator


class URLCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    long_url: str = Field(..., alias="url", description="The long URL to shorten")
    name: Optional[str] = Field(None, description="Optional name or alias")

    @field_validator("long_url", mode="before")
    @classmethod
    def validate_and_normalize_url(cls, v: str) -> str:
        if not isinstance(v, str):
            raise ValueError("URL must be a string")
        v = v.strip()
        if not v.startswith(("http://", "https://")):
            v = "https://" + v
        return v


class URLResponse(BaseModel):
    short_url: str
    long_url: str
