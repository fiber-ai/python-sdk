"""Default x-client-* headers that let the Fiber AI API attribute usage to this SDK.

Hand-written (not generated). Wired into ``Client`` and ``AuthenticatedClient`` by
``templates/client.py.jinja``, so it survives regeneration.
"""

from importlib.metadata import PackageNotFoundError, version


def _sdk_version() -> str:
    try:
        return version("fiberai")
    except PackageNotFoundError:
        return "unknown"


CLIENT_ATTRIBUTION_HEADERS: dict[str, str] = {
    "x-client-type": "SDK",
    "x-client-name": f"fiberai-python/{_sdk_version()}",
}


def with_client_attribution_headers(headers: dict[str, str]) -> dict[str, str]:
    """Return ``headers`` with attribution defaults added; caller-supplied values win (case-insensitively)."""
    overridden: set[str] = {name.lower() for name in headers}
    defaults: dict[str, str] = {
        name: value for name, value in CLIENT_ATTRIBUTION_HEADERS.items() if name not in overridden
    }
    return {**defaults, **headers}
