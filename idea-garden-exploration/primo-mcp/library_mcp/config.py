import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Find .env next to this project, wherever Claude starts us from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    server_name: str
    max_results: int


def get_settings() -> Settings:
    return Settings(
        server_name=os.getenv("SERVER_NAME", "Library Research Toolkit"),
        max_results=int(os.getenv("MAX_RESULTS", "5")),
    )