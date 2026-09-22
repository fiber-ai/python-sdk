from enum import StrEnum


class BasicWorkEmailRevealBodyNameType1Mode(StrEnum):
    FIRSTLAST = "firstLast"

    def __str__(self) -> str:
        return str(self.value)
