from enum import Enum


class CompanyCountBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
