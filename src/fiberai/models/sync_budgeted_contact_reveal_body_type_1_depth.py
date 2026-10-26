from enum import StrEnum


class SyncBudgetedContactRevealBodyType1Depth(StrEnum):
    QUICK = "quick"

    def __str__(self) -> str:
        return str(self.value)
