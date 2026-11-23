from enum import StrEnum


class CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
