"""MockFixture tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mock_fixture import streams

class TapMockFixture(Tap):
    """MockFixture tap class."""

    name = "tap-mock-fixture"

    config_jsonschema = th.PropertiesList().to_dict()

    def discover_streams(self) -> list[streams.MockStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.UsersStream(self),
            streams.AnimalsStream(self),
        ]


if __name__ == "__main__":
    TapMockFixture.cli()
