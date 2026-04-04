from enum import Enum


class GetScoutingReportResponse200OutputReportMediaLinksItemType(str, Enum):
    PODCAST = "podcast"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
