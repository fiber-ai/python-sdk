from enum import StrEnum


class CompanySearchResponse200OutputDataItemMatchesType0JobPostingsType0PostingsItemStatus(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
