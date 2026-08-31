from enum import StrEnum


class ListAllProfilesFromJobChangeListResponse200OutputProfilesItemAllMovementsItemMovement(StrEnum):
    CHANGED = "changed"
    LATERAL_MOVE = "lateral-move"
    NEW_ROLE = "new-role"
    NO_CHANGE = "no-change"
    PROMOTED = "promoted"

    def __str__(self) -> str:
        return str(self.value)
