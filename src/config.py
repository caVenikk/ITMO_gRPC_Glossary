from functools import lru_cache
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    database_url: str = os.getenv("DATABASE_URL")
    debug: bool = os.getenv("DEBUG") == "True"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
