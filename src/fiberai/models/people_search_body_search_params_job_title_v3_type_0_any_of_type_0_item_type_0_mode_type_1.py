from enum import StrEnum


class PeopleSearchBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1(StrEnum):
    NORMAL = "normal"
    PHRASE = "phrase"
    PREFIX = "prefix"

    def __str__(self) -> str:
        return str(self.value)
