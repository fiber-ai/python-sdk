from enum import StrEnum


class BuildAudienceResponse200OutputStatus(StrEnum):
    BUILDING = "BUILDING"

    def __str__(self) -> str:
        return str(self.value)
