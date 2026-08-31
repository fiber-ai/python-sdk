from enum import StrEnum


class GetTechnologiesResponse200OutputItemType(StrEnum):
    PLATFORM = "platform"
    TECHNOLOGY = "technology"

    def __str__(self) -> str:
        return str(self.value)
