from enum import Enum


class CompanyLocationChangeChangeTypeType2Type1(str, Enum):
    ADDED = "added"

    def __str__(self) -> str:
        return str(self.value)
