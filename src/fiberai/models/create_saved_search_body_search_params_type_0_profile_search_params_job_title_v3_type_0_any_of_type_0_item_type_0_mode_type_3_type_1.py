from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1(
    StrEnum
):
    NORMAL = "normal"
    PHRASE = "phrase"
    PREFIX = "prefix"

    def __str__(self) -> str:
        return str(self.value)
