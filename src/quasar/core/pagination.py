"""Cursor helpers for paginated endpoints."""

from typing import Any, Callable, Dict, Iterator, List

from quasar.core.compat import deprecated


class Paginator:
    """Iterate over cursor-based pages."""

    def __init__(self, page_size: int = 100) -> None:
        self.page_size = page_size

    def pages(self, fetch: Callable[..., List[Dict[str, Any]]]) -> Iterator[List[Dict[str, Any]]]:
        cursor = None
        while True:
            page = fetch(cursor, self.page_size)
            if not page:
                return
            yield page
            cursor = page[-1].get("cursor")


@deprecated(since="2.3", remove_in="2.7", replacement="Paginator")
def page_walk(fetch: Callable[..., List[Dict[str, Any]]], page_size: int = 50) -> List[Dict[str, Any]]:
    """Collect every record by walking ``fetch`` page by page."""
    records: List[Dict[str, Any]] = []
    for page in Paginator(page_size).pages(fetch):
        records.extend(page)
    return records
