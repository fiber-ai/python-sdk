from enum import Enum


class PersonBecamePremiumDirection(str, Enum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
