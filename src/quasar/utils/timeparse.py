"""Timestamp parsing utilities."""

from datetime import datetime, timezone
from typing import Optional

from quasar.core.compat import deprecated


def parse_timestamp(value: str) -> datetime:
    """Parse an RFC 3339 timestamp into an aware ``datetime``."""
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


@deprecated(since="2.3", remove_in="2.5", replacement="parse_timestamp")
def parse_iso(value: str, assume_utc: bool = False) -> Optional[datetime]:
    """Parse an ISO-8601 string, tolerating a missing offset."""
    if assume_utc and not value.endswith("Z") and "+" not in value:
        value = value + "+00:00"
    try:
        return parse_timestamp(value)
    except ValueError:
        return None
