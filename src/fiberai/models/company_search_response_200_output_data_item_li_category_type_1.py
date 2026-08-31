from enum import StrEnum


class CompanySearchResponse200OutputDataItemLiCategoryType1(StrEnum):
    C = "C"
    S = "S"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
