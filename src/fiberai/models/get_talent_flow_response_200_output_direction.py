from enum import Enum


class GetTalentFlowResponse200OutputDirection(str, Enum):
    JOINERS = "joiners"
    LEAVERS = "leavers"

    def __str__(self) -> str:
        return str(self.value)
