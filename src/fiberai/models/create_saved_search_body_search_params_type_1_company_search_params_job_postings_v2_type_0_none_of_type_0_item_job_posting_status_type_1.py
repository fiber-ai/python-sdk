from enum import StrEnum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingsV2Type0NoneOfType0ItemJobPostingStatusType1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
