from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemDirection(str, Enum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
