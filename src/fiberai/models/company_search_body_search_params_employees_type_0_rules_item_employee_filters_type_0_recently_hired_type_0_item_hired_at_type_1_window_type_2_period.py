from enum import Enum


class CompanySearchBodySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Period(
    str, Enum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
