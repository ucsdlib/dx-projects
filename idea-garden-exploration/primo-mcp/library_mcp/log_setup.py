import logging
import os
import sys


def setup_logging() -> None:
    logging.basicConfig(
        stream=sys.stderr,
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s%(levelname)s%(name)s:%(message)s",
    )
