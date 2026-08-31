from enum import StrEnum


class PollDepthChartResponse200OutputType1Status(StrEnum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
