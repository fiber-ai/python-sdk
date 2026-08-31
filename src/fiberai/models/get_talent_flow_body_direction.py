from enum import StrEnum


class GetTalentFlowBodyDirection(StrEnum):
    JOINERS = "joiners"
    LEAVERS = "leavers"

    def __str__(self) -> str:
        return str(self.value)
