from enum import StrEnum


class CompanyLocationChangeChangeTypeType1(StrEnum):
    ADDED = "added"

    def __str__(self) -> str:
        return str(self.value)
