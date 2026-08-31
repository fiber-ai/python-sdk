from enum import StrEnum


class CompanySearchBodySearchParamsLastFundedOnType1Strategy(StrEnum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
