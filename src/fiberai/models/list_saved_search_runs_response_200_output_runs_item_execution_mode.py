from enum import Enum

class ListSavedSearchRunsResponse200OutputRunsItemExecutionMode(str, Enum):
    AUTOMATICALLY_TRIGGERED = "automatically_triggered"
    MANUALLY_TRIGGERED = "manually_triggered"

    def __str__(self) -> str:
        return str(self.value)
