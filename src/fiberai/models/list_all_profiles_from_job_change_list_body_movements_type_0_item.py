from enum import Enum


class ListAllProfilesFromJobChangeListBodyMovementsType0Item(str, Enum):
    CHANGED = "changed"
    LATERAL_MOVE = "lateral-move"
    NEW_ROLE = "new-role"
    NO_CHANGE = "no-change"
    PROMOTED = "promoted"

    def __str__(self) -> str:
        return str(self.value)
