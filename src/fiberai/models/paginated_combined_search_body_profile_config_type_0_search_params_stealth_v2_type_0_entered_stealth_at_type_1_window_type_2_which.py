from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
