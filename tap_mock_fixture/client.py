"""Custom client handling, including MockFixtureStream base class."""

from __future__ import annotations

from typing import Iterable

from singer_sdk.streams import Stream


class MockStream(Stream):
    """Stream class for MockStream streams."""

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
        raise NotImplementedError
