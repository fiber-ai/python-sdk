from enum import Enum


class GetTrackerOverviewResponse200OutputCompanyListsItemEntityType(str, Enum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
