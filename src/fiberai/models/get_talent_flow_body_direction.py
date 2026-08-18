from enum import Enum


class GetTalentFlowBodyDirection(str, Enum):
    JOINERS = "joiners"
    LEAVERS = "leavers"

    def __str__(self) -> str:
        return str(self.value)
