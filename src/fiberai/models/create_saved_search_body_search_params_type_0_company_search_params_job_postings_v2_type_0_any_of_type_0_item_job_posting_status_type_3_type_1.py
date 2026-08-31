from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
