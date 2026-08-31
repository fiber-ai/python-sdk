from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0NoneOfType0ItemJobPostingStatusType1(
    StrEnum
):
    ACTIVE = "active"
    CLOSED = "closed"
    EITHER = "either"

    def __str__(self) -> str:
        return str(self.value)
