from enum import Enum


class CompanyLocationChangeChangeTypeType1(str, Enum):
    ADDED = "added"

    def __str__(self) -> str:
        return str(self.value)
