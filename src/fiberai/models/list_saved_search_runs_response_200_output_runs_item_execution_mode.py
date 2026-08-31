from enum import StrEnum


class ListSavedSearchRunsResponse200OutputRunsItemExecutionMode(StrEnum):
    AUTOMATICALLY_TRIGGERED = "automatically_triggered"
    MANUALLY_TRIGGERED = "manually_triggered"

    def __str__(self) -> str:
        return str(self.value)
