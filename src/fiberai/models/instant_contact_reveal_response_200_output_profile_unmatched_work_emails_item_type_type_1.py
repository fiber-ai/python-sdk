from enum import StrEnum


class InstantContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemTypeType1(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
