"""Asynchronous transport helpers."""

import asyncio
from typing import Any, Dict

from quasar.core.compat import deprecated


class AsyncHttpClient:
    """Asyncio transport that mirrors :class:`quasar.clients.http.HttpClient`."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    async def request(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0)
        return {"path": path, "payload": payload}


@deprecated(since="2.4", remove_in="3.0", replacement="AsyncHttpClient")
class AsyncSocketAdapter:
    """Raw-socket adapter kept for the 2.2 async transport."""

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    async def send(self, payload: bytes) -> int:
        return len(payload)
