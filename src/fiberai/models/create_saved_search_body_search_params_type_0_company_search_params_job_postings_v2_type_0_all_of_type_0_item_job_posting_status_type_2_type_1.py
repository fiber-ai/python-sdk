from enum import Enum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsJobPostingsV2Type0AllOfType0ItemJobPostingStatusType2Type1(
    str, Enum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
