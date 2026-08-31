from enum import StrEnum


class PostSearchByKeywordsBodyRecencyType1(StrEnum):
    DAY = "Day"
    HALFYEAR = "HalfYear"
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
