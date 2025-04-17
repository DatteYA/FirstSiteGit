from pydantic_settings import BaseSettings
from pathlib import Path

#BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    apiv1_prefix: str = "/api/v1"
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = True
    # db_echo: bool = False


settings = Settings()
