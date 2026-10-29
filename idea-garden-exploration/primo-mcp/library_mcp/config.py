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
    primo_base_url: str
    primo_api_key: str
    primo_vid: str
    primo_tab: str
    primo_scope: str
    primo_discovery_url: str


def get_settings() -> Settings:
    return Settings(
        server_name=os.getenv("SERVER_NAME", "Library Research Toolkit"),
        max_results=int(os.getenv("MAX_RESULTS", "5")),
        primo_base_url=os.getenv("PRIMO_BASE_URL", "http://127.0.0.1:8001"),
        primo_api_key=os.getenv("PRIMO_API_KEY", ""),
        primo_vid=os.getenv("PRIMO_VID", ""),
        primo_tab=os.getenv("PRIMO_TAB", ""),
        primo_scope=os.getenv("PRIMO_SCOPE", ""),
        primo_discovery_url=os.getenv("PRIMO_DISCOVERY_URL", ""),
    )