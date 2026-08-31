from enum import StrEnum


class CompanySearchBodySearchParamsEmployeesType0RulesItemJobStatusType1LeftAtType1WindowType0Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
