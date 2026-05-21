from enum import Enum


class LiteContactRevealResponse200OutputProfileEmailsItemTypeType1(str, Enum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
