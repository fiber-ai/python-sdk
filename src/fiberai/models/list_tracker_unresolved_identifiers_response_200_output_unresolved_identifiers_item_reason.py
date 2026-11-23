from enum import StrEnum


class ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItemReason(StrEnum):
    PROFILE_NOT_FOUND = "profile_not_found"

    def __str__(self) -> str:
        return str(self.value)
