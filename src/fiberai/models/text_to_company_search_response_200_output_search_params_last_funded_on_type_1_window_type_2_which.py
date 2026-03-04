from enum import Enum

class TextToCompanySearchResponse200OutputSearchParamsLastFundedOnType1WindowType2Which(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
