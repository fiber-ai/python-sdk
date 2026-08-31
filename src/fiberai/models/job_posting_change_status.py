from enum import StrEnum


class JobPostingChangeStatus(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
