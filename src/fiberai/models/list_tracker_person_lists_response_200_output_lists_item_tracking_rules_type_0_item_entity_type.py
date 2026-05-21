from enum import Enum


class ListTrackerPersonListsResponse200OutputListsItemTrackingRulesType0ItemEntityType(str, Enum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
