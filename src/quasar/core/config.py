"""Configuration loading for the SDK."""

import os
from typing import Any, Dict, Mapping

from quasar.core.compat import deprecated


class ConfigLoader:
    """Resolve SDK settings from a mapping or the process environment."""

    def __init__(self, values: Mapping[str, Any] = None) -> None:
        self._values: Dict[str, Any] = dict(values or {})

    def get(self, key: str, default: Any = None) -> Any:
        return self._values.get(key, default)

    @classmethod
    def from_env(cls, prefix: str = "QUASAR_") -> "ConfigLoader":
        values = {
            key[len(prefix):].lower(): value
            for key, value in os.environ.items()
            if key.startswith(prefix)
        }
        return cls(values)


@deprecated(since="2.3", remove_in="2.5", replacement="ConfigLoader.from_env")
def load_env_config(prefix: str = "QUASAR_") -> ConfigLoader:
    """Build a :class:`ConfigLoader` from environment variables."""
    return ConfigLoader.from_env(prefix)
