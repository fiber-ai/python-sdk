from enum import StrEnum


class PersonBecameInfluencerDirection(StrEnum):
    EITHER = "either"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
