from enum import StrEnum


class UpdateTrackerEntityLimitBodyEntityType(StrEnum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
