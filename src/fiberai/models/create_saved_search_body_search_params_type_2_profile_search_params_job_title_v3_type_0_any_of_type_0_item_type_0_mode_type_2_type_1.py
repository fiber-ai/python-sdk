from enum import StrEnum


class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1(
    StrEnum
):
    NORMAL = "normal"
    PHRASE = "phrase"
    PREFIX = "prefix"

    def __str__(self) -> str:
        return str(self.value)
