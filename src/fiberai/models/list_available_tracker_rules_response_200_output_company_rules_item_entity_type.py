from enum import Enum


class ListAvailableTrackerRulesResponse200OutputCompanyRulesItemEntityType(str, Enum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
