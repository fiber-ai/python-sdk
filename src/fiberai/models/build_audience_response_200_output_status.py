from enum import Enum


class BuildAudienceResponse200OutputStatus(str, Enum):
    BUILDING = "BUILDING"

    def __str__(self) -> str:
        return str(self.value)
