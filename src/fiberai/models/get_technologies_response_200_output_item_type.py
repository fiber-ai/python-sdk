from enum import Enum


class GetTechnologiesResponse200OutputItemType(str, Enum):
    PLATFORM = "platform"
    TECHNOLOGY = "technology"

    def __str__(self) -> str:
        return str(self.value)
