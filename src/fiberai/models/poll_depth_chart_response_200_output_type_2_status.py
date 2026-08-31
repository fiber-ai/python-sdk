from enum import StrEnum


class PollDepthChartResponse200OutputType2Status(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
