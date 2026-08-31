from enum import StrEnum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
