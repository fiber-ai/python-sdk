from enum import Enum


class PostSearchByKeywordsBodyRecencyType1(str, Enum):
    DAY = "Day"
    HALFYEAR = "HalfYear"
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
