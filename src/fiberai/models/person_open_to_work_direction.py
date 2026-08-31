from enum import StrEnum


class PersonOpenToWorkDirection(StrEnum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
