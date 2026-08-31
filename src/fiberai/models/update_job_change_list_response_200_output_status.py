from enum import StrEnum


class UpdateJobChangeListResponse200OutputStatus(StrEnum):
    BUILDING = "BUILDING"
    DRAFT = "DRAFT"
    ERROR = "ERROR"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
