from enum import Enum


class SyncQuickContactRevealResponse200OutputProfileStatus(str, Enum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
