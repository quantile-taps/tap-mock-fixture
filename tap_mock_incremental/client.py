"""Custom client handling, including MockIncrementalStream base class."""

from __future__ import annotations

from typing import Iterable

from singer_sdk.streams import Stream


class MockIncrementalStream(Stream):
    """Stream class for MockIncremental streams."""

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

        Raises:
            NotImplementedError: If the implementation is TODO
        """
        records = [
            {"id": 1, "name": "A", "updated_at": "2023-01-01"},
            {"id": 2, "name": "B", "updated_at": "2023-02-01"},
            {"id": 3, "name": "C", "updated_at": "2023-03-01"},
        ]

        for record in records:
            yield record 
