from enum import StrEnum


class CombinedSearchCountBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
