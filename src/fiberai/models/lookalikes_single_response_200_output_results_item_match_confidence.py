from enum import StrEnum


class LookalikesSingleResponse200OutputResultsItemMatchConfidence(StrEnum):
    DEFINITE = "definite"
    LIKELY = "likely"
    STRETCH = "stretch"

    def __str__(self) -> str:
        return str(self.value)
