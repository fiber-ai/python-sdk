from enum import StrEnum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingsV2Type0AllOfType0ItemJobPostingStatusType3Type1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
