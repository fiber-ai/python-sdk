from enum import StrEnum


class JobPostingSearchResponse200OutputDataItemStatus(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
