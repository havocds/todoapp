from pydantic import BaseModel


class Healthz(BaseModel):
    name: str
    api_version: str
    status: str = "OK"
