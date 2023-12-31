from pydantic import BaseModel


class Healthz(BaseModel):
    name: str
    status: str = "OK"
