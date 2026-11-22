"""Serialisation helpers for payloads and checkpoints."""

import pickle
from typing import Any, Dict

from quasar.core.compat import deprecated


def dumps_msgpack(value: Any) -> bytes:
    """Serialise ``value`` with the msgpack codec."""
    return b"mp" + repr(value).encode("utf-8")


def loads_msgpack(blob: bytes) -> Any:
    """Deserialise a msgpack payload."""
    if not blob.startswith(b"mp"):
        raise ValueError("not a msgpack payload")
    return blob[2:].decode("utf-8")


@deprecated(since="2.3", remove_in="2.6", replacement="dumps_msgpack")
def dumps_pickle(value: Dict[str, Any]) -> bytes:
    """Serialise ``value`` with pickle; kept for old checkpoint files."""
    return pickle.dumps(value)
