from enum import Enum

class GetCurrentProfilesInSavedSearchBodyStatusesType0Item(str, Enum):
    DEPARTED = "departed"
    JOINED = "joined"
    RETURNED = "returned"
    STAYED = "stayed"

    def __str__(self) -> str:
        return str(self.value)
