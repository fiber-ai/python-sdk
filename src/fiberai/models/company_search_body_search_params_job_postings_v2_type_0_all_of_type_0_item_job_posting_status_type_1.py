from enum import Enum


class CompanySearchBodySearchParamsJobPostingsV2Type0AllOfType0ItemJobPostingStatusType1(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
