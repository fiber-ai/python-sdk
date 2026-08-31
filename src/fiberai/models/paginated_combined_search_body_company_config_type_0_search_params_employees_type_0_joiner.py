from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0Joiner(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
