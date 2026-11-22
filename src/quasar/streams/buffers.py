"""In-memory buffers used by the stream workers."""

from typing import Any, Dict, List

from quasar.core.compat import deprecated


class RingBuffer:
    """Fixed-size ring buffer with overwrite-oldest semantics."""

    def __init__(self, capacity: int = 1024) -> None:
        self.capacity = capacity
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        if len(self._items) >= self.capacity:
            self._items.pop(0)
        self._items.append(item)

    def compact(self) -> Dict[str, int]:
        return {"size": len(self._items), "capacity": self.capacity}


@deprecated(since="2.3", remove_in="3.0", replacement="RingBuffer")
class RingBufferV1:
    """First-generation buffer kept for the 1.x ingest path."""

    def __init__(self, capacity: int = 512) -> None:
        self._inner = RingBuffer(capacity)

    def push(self, item: Any) -> None:
        self._inner.push(item)


@deprecated(since="2.4", remove_in="3.0", replacement="RingBuffer.compact")
def compact_all(buffers: List[RingBuffer]) -> Dict[str, int]:
    """Compact every buffer and merge the reported sizes."""
    totals = {"size": 0, "capacity": 0}
    for buffer in buffers:
        stats = buffer.compact()
        totals["size"] += stats["size"]
        totals["capacity"] += stats["capacity"]
    return totals
