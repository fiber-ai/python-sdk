from enum import Enum


class PollDepthChartResponse200OutputType2Status(str, Enum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
