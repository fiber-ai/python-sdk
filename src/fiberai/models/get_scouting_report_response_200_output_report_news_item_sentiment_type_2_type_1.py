from enum import StrEnum


class GetScoutingReportResponse200OutputReportNewsItemSentimentType2Type1(StrEnum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"

    def __str__(self) -> str:
        return str(self.value)
