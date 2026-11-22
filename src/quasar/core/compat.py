"""Deprecation helpers shared across the SDK."""

import functools
import warnings


def deprecated(since: str, remove_in: str, replacement: str = ""):
    """Mark a public symbol as deprecated.

    ``since`` is the release that introduced the warning, ``remove_in`` the
    first release in which the symbol may disappear and ``replacement`` the
    dotted name callers should migrate to.
    """

    def decorator(obj):
        message = f"{obj.__name__} is deprecated since {since}"
        if remove_in:
            message += f" and will be removed in {remove_in}"
        if replacement:
            message += f"; use {replacement} instead"

        @functools.wraps(obj)
        def wrapper(*args, **kwargs):
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return obj(*args, **kwargs)

        return wrapper

    return decorator
