from enum import StrEnum


class CreateTrackerCompanyListBodyCompanySearchParamsType0EmployeesType0Joiner(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
