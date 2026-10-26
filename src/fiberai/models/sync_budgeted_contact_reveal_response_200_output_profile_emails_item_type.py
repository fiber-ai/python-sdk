from enum import StrEnum


class SyncBudgetedContactRevealResponse200OutputProfileEmailsItemType(StrEnum):
    PERSONAL = "personal"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
