from enum import Enum


class TrackerSignalDeliveryStatus(str, Enum):
    DELIVERED = "DELIVERED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
