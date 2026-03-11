from enum import Enum


class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiCategoryType1(str, Enum):
    C = "C"
    S = "S"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
