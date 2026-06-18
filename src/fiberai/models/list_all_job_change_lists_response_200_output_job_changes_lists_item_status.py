from enum import Enum


class ListAllJobChangeListsResponse200OutputJobChangesListsItemStatus(str, Enum):
    BUILDING = "BUILDING"
    DRAFT = "DRAFT"
    ERROR = "ERROR"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
