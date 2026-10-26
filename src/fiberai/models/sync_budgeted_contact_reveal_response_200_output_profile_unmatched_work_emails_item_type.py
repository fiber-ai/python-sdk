from enum import StrEnum


class SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemType(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
