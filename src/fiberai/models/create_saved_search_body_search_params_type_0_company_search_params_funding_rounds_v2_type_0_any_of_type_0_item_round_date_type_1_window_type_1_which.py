from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1WindowType1Which(
    StrEnum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
