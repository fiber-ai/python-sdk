from enum import StrEnum


class ListAllJobChangeListsResponse200OutputJobChangesListsItemStatus(StrEnum):
    BUILDING = "BUILDING"
    DRAFT = "DRAFT"
    ERROR = "ERROR"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
