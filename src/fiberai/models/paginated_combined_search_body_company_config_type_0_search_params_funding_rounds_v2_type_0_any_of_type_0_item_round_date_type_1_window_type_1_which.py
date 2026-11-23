from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1WindowType1Which(
    StrEnum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
