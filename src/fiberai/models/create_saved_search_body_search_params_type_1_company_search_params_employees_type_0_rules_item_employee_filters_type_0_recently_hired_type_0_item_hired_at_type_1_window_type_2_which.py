from enum import Enum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
