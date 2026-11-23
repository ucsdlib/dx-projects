import logging
import os
import sys


def setup_logging() -> None:
    logging.basicConfig(
        stream=sys.stderr,
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    # httpx2 logs full request URLs at INFO, and those URLs contain the search text.
    logging.getLogger("httpx2").setLevel(logging.WARNING)
