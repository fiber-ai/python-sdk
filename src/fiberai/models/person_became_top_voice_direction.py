from enum import StrEnum


class PersonBecameTopVoiceDirection(StrEnum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
