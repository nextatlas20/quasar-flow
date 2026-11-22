"""Synchronous HTTP transport for the Quasar Flow gateway."""

import json
from typing import Any, Dict

from quasar.core.compat import deprecated


class HttpClient:
    """Pooled transport used by the 2.x public client."""

    def __init__(self, base_url: str, pool_size: int = 8) -> None:
        self.base_url = base_url.rstrip("/")
        self.pool_size = pool_size

    def request(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("the managed transport is injected at runtime")


@deprecated(since="2.3", remove_in="2.6", replacement="HttpClient")
class LegacySession:
    """Session object kept alive for the 1.x call sites."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def send(self, path: str, payload: Dict[str, Any]) -> str:
        return json.dumps({"path": path, "payload": payload})


@deprecated(since="2.3", remove_in="2.6", replacement="HttpClient.request")
def open_legacy(base_url: str) -> LegacySession:
    """Build a ``LegacySession`` for older integrations."""
    return LegacySession(base_url)
