from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(
    StrEnum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
