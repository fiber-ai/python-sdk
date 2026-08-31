from enum import StrEnum


class LiteContactRevealResponse200OutputProfileEmailsItemTypeType3Type1(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
