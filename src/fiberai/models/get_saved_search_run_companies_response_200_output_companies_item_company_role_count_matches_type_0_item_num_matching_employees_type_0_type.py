from enum import Enum


class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyRoleCountMatchesType0ItemNumMatchingEmployeesType0Type(
    str, Enum
):
    EXACT = "exact"

    def __str__(self) -> str:
        return str(self.value)
