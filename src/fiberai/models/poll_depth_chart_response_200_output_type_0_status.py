from enum import StrEnum


class PollDepthChartResponse200OutputType0Status(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
