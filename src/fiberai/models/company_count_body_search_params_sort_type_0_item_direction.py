from enum import StrEnum


class CompanyCountBodySearchParamsSortType0ItemDirection(StrEnum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
