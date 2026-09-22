from enum import StrEnum


class BasicWorkEmailRevealResponse200OutputEmailsItemTypeType1(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
