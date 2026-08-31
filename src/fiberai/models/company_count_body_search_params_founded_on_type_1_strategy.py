from enum import StrEnum


class CompanyCountBodySearchParamsFoundedOnType1Strategy(StrEnum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
