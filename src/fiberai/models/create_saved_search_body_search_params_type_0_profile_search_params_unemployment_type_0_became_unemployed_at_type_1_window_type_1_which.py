from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(
    StrEnum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
