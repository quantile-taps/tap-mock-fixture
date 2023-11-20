"""Stream type classes for tap-mock-incremental."""

from __future__ import annotations

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mock_incremental.client import MockIncrementalStream

class UsersStream(MockIncrementalStream):
    """Define custom stream."""

    name = "users"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

