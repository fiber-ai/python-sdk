from enum import Enum


class TextToCombinedSearchResponse200OutputCompanySearchParamsType0InvestorsV2Type0AnyOfType0ItemInvestedAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
