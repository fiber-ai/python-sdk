from enum import Enum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsEmployeesType0Joiner(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
