from enum import Enum

class GetSavedSearchRunProfilesBodyStatusesType0Item(str, Enum):
    DEPARTED = "departed"
    JOINED = "joined"
    RETURNED = "returned"
    STAYED = "stayed"

    def __str__(self) -> str:
        return str(self.value)
