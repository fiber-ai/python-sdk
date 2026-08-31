from enum import StrEnum


class GetTalentFlowResponse200OutputDirection(StrEnum):
    JOINERS = "joiners"
    LEAVERS = "leavers"

    def __str__(self) -> str:
        return str(self.value)
