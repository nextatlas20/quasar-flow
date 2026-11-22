"""Windowed aggregation for stream operators."""

from typing import Any, Dict, List

from quasar.core.compat import deprecated


class WindowAggregator:
    """Tumbling-window aggregator with pluggable reducers."""

    def __init__(self, size: int = 60) -> None:
        self.size = size
        self._buckets: Dict[int, List[Any]] = {}

    def add(self, timestamp: int, value: Any) -> None:
        bucket = timestamp // self.size
        self._buckets.setdefault(bucket, []).append(value)

    def snapshot(self) -> Dict[int, List[Any]]:
        return {bucket: list(values) for bucket, values in self._buckets.items()}


@deprecated(since="2.3", remove_in="2.6", replacement="WindowAggregator")
class WindowAggregatorSimple:
    """Single-bucket aggregator used by the 2.2 pipeline templates."""

    def __init__(self) -> None:
        self._values: List[Any] = []

    def add(self, value: Any) -> None:
        self._values.append(value)
