from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AllOfType0ItemType0ModeType2Type1(
    StrEnum
):
    NORMAL = "normal"
    PHRASE = "phrase"
    PREFIX = "prefix"

    def __str__(self) -> str:
        return str(self.value)
