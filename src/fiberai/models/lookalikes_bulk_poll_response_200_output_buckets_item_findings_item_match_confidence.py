from enum import StrEnum


class LookalikesBulkPollResponse200OutputBucketsItemFindingsItemMatchConfidence(StrEnum):
    DEFINITE = "definite"
    LIKELY = "likely"
    STRETCH = "stretch"

    def __str__(self) -> str:
        return str(self.value)
