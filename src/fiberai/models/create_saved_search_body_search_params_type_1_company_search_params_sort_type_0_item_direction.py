from enum import Enum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsSortType0ItemDirection(str, Enum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
