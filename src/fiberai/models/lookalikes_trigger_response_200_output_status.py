from enum import StrEnum


class LookalikesTriggerResponse200OutputStatus(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
