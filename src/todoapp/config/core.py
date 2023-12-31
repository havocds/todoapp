from pathlib import Path
from typing import List

from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

CONFIG_PATH = Path(__file__).resolve().parent
CONFIG_FILE = CONFIG_PATH / "config.yaml"
PACKAGE_PATH = CONFIG_PATH.parent
ROOT_PATH = PACKAGE_PATH.parent.parent

TEMPLATES_PATH = PACKAGE_PATH / "templates"
INDEX_HTML = TEMPLATES_PATH / "index.html"


class Settings(BaseSettings):
    APP_NAME: str = "todoapp"
    API_V1_STR: str = "/api/v1"
    MONGODB_URL: str = config("MONGODB_URL")
    MONGODB_URI: str = config("MONGODB_URI")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # type: ignore
        "http://localhost:8000",  # type: ignore
        "http://localhost:5173",  # type: ignore
        "https://localhost:3000",  # type: ignore
        "https://localhost:8000",  # type: ignore
        "https://localhost:5173",  # type: ignore
    ]

    model_config = SettingsConfigDict(
        case_sensitive=True,
    )


settings = Settings()
