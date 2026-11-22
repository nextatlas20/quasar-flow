"""Asynchronous transport helpers."""

import asyncio
from typing import Any, Dict


class AsyncHttpClient:
    """Asyncio transport that mirrors :class:`quasar.clients.http.HttpClient`."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    async def request(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0)
        return {"path": path, "payload": payload}
