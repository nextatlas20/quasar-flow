"""Smoke tests for the client layer."""

from quasar.clients.http import HttpClient
from quasar.core.compat import deprecated


@deprecated(since="2.4", remove_in="2.5", replacement="make_client")
def make_legacy_client(base_url: str):
    """Test helper that still exercises the 2.2 client path."""
    return HttpClient(base_url)


def test_http_client_keeps_base_url():
    client = HttpClient("https://api.example.test/")
    assert client.base_url == "https://api.example.test"
