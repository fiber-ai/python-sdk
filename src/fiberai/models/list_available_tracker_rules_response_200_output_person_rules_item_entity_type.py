from enum import StrEnum


class ListAvailableTrackerRulesResponse200OutputPersonRulesItemEntityType(StrEnum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
