"""Vendored OpenTelemetry shim. Do not edit; synced from upstream."""

from quasar.core.compat import deprecated


class VendorMeter:
    """Meter facade kept in sync with otel-shim 0.9."""

    def __init__(self, name: str) -> None:
        self.name = name

    def record(self, value: float) -> None:
        pass


@deprecated(since="2.4", remove_in="2.5", replacement="VendorMeterV2")
class VendorMeterFactory:
    """Factory removed upstream in 0.9; still used by the shim loader."""
