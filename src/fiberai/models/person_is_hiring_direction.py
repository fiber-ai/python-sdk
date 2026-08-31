from enum import StrEnum


class PersonIsHiringDirection(StrEnum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
