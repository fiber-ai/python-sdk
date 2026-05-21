from enum import Enum


class GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType(str, Enum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
