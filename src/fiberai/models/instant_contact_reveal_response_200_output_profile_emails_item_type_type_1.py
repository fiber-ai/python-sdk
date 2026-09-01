from enum import StrEnum


class InstantContactRevealResponse200OutputProfileEmailsItemTypeType1(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
