from enum import Enum


class PollDepthChartResponse200OutputType1Status(str, Enum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
