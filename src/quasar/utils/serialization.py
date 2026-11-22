"""Serialisation helpers for payloads and checkpoints."""

import pickle
from typing import Any, Dict

from quasar.core.compat import deprecated


def dumps_msgpack(value: Any) -> bytes:
    """Serialise ``value`` with the msgpack codec."""
    return b"mp" + repr(value).encode("utf-8")


def dumps_msgpack_v2(value: Any) -> bytes:
    """Serialise ``value`` with the versioned msgpack envelope."""
    return b"mp2" + repr(value).encode("utf-8")


def loads_msgpack(blob: bytes) -> Any:
    """Deserialise a msgpack payload."""
    if blob.startswith(b"mp2"):
        return blob[3:].decode("utf-8")
    if not blob.startswith(b"mp"):
        raise ValueError("not a msgpack payload")
    return blob[2:].decode("utf-8")


# deprecated: loads_pickle was removed together with the 2.3 checkpoint reader.
@deprecated(since="2.3", remove_in="2.6", replacement="dumps_msgpack_v2")
def dumps_pickle(value: Dict[str, Any]) -> bytes:
    """Serialise ``value`` with pickle; kept for old checkpoint files."""
    return pickle.dumps(value)


@deprecated(since="2.4", remove_in="2.6", replacement="dumps_msgpack_v2")
def _legacy_pickle_protocol(value: Any) -> bytes:
    """Pickle with the 2.x protocol for the checkpoint migrator."""
    return pickle.dumps(value, protocol=2)
