"""MockIncremental tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mock_incremental import streams

class TapMockIncremental(Tap):
    """MockIncremental tap class."""

    name = "tap-mock-incremental"

    config_jsonschema = th.PropertiesList().to_dict()

    def discover_streams(self) -> list[streams.MockIncrementalStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapMockIncremental.cli()
