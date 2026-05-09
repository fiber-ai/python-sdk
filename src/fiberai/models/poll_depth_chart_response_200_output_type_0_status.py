from enum import Enum


class PollDepthChartResponse200OutputType0Status(str, Enum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
