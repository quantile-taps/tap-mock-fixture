"""Stream type classes for tap-mock-fixture."""

from __future__ import annotations

from singer_sdk import typing as th  # JSON Schema typing helpers
from typing import Iterable

from tap_mock_fixture.client import MockStream

class UsersStream(MockStream):
    """Define custom stream."""

    name = "users"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.
        """
        records = [
            {"id": 1, "name": "Piet", "updated_at": "2023-01-01"},
            {"id": 2, "name": "Jan", "updated_at": "2023-02-01"},
            {"id": 3, "name": "Klaas", "updated_at": "2023-03-01"},
        ]

        for record in records:
            yield record 

class AnimalsStream(MockStream):
    """Define custom stream."""

    name = "animals"
    primary_keys = ["id"]
    selected_by_default = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("animal_name", th.StringType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.
        """
        records = [
            {"id": 1, "animal_name": "Monkey", "updated_at": "2023-01-01"},
            {"id": 2, "animal_name": "Bear", "updated_at": "2023-02-01"},
            {"id": 3, "animal_name": "Koala", "updated_at": "2023-03-01"},
        ]

        for record in records:
            yield record 

