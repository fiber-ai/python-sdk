from enum import Enum


class SocialMediaLookupPollingResponse200OutputStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
