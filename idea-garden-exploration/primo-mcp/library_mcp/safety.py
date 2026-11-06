import re
from typing import overload

MAX_FIELD_CHARS = 300
_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")


def clean_query(text: str) -> str:
    """Make user search words safe for Primo's q=field,precision,value format."""
    text = _CONTROL_CHARS.sub(" ", text)
    text = text.replace(",", " ").replace(";", " ")
    return " ".join(text.split())[:200]


@overload
def tidy(text: str) -> str: ...
@overload
def tidy(text: None) -> None: ...
def tidy(text: str | None) -> str | None:
    """Trim and shorten untrusted metadata before it reaches the AI."""
    if text is None:
        return None
    text = " ".join(_CONTROL_CHARS.sub(" ", text).split())
    return text[:MAX_FIELD_CHARS]