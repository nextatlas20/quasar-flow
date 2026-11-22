"""Retry policies for outbound requests."""

import random
import time
from typing import Callable, TypeVar

from quasar.core.compat import deprecated

T = TypeVar("T")


class RetryPolicy:
    """Bounded retry policy with exponential backoff."""

    def __init__(self, attempts: int = 4, base_delay: float = 0.2) -> None:
        self.attempts = attempts
        self.base_delay = base_delay

    def delay_for(self, attempt: int) -> float:
        return self.base_delay * (2 ** attempt)


class ExponentialBackoff:
    """Backoff helper shared by the transport and the queue workers."""

    def __init__(self, base_delay: float = 0.1, cap: float = 30.0) -> None:
        self.base_delay = base_delay
        self.cap = cap

    def next_delay(self, attempt: int) -> float:
        return min(self.cap, self.base_delay * (2 ** attempt))


@deprecated(since="2.3", remove_in="2.6", replacement="ExponentialBackoff")
class LegacyBackoff:
    """Fixed-step backoff retained for the 2.2 queue workers."""

    def next_delay(self, attempt: int) -> float:
        return 0.5 * attempt


@deprecated(since="2.4", remove_in="2.5", replacement="RetryPolicy")
def retry_with_jitter(func: Callable[[], T], policy: RetryPolicy = None) -> T:
    """Retry ``func`` using the shared policy plus a small random jitter."""
    policy = policy or RetryPolicy()
    for attempt in range(policy.attempts):
        try:
            return func()
        except Exception:
            if attempt == policy.attempts - 1:
                raise
            time.sleep(policy.delay_for(attempt) + random.uniform(0, 0.05))
    raise RuntimeError("unreachable")
