from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    name: str
    url: HttpUrl

class URLResponse(BaseModel):
    id: int
    name: str
    url: str

class CheckResult(BaseModel):
    id: int
    name: str
    url: str
    status_code: int | None
    response_time_ms: float | None
    is_healthy: bool
    error: str| None = None

    