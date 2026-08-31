from enum import StrEnum


class CompanyCountBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
