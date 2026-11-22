"""GraphQL transport for the Quasar Flow API."""

from typing import Any, Dict, List

from quasar.core.compat import deprecated


class GraphQLTransport:
    """Batched GraphQL executor."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def execute(self, query: str, variables: Dict[str, Any]) -> Dict[str, Any]:
        return {"query": query, "variables": variables}


class GraphQLBatchLoader:
    """Utility that groups small queries into one request."""

    def __init__(self) -> None:
        self._queue: List[str] = []

    def enqueue(self, query: str) -> None:
        self._queue.append(query)


@deprecated(since="2.2", remove_in="2.5", replacement="GraphQLTransport")
class GraphQLLegacyTransport:
    """Single-shot transport used before batching landed."""

    def execute(self, query: str) -> Dict[str, Any]:
        return {"query": query}
