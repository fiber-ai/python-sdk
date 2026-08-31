from enum import StrEnum


class GetTrackerOverviewResponse200OutputUpcomingRefreshesItemEntityType(StrEnum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
