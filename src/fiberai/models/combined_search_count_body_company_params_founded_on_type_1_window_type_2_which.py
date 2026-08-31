from enum import StrEnum


class CombinedSearchCountBodyCompanyParamsFoundedOnType1WindowType2Which(StrEnum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
