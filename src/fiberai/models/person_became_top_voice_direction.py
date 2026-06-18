from enum import Enum


class PersonBecameTopVoiceDirection(str, Enum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
