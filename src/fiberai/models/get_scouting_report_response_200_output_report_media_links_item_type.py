from enum import StrEnum


class GetScoutingReportResponse200OutputReportMediaLinksItemType(StrEnum):
    PODCAST = "podcast"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
