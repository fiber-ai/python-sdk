from enum import Enum


class BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
