from enum import StrEnum


class CombinedSearchCountBodyCompanyParamsEmployeesType0Joiner(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
