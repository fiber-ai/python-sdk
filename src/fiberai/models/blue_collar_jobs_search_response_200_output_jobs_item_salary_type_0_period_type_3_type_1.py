from enum import StrEnum


class BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1(StrEnum):
    DAILY = "daily"
    HOURLY = "hourly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
