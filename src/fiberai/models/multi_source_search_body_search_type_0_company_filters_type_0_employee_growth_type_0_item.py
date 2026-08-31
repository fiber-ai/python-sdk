from enum import StrEnum


class MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item(StrEnum):
    DECLINING = "declining"
    GROWING = "growing"
    HIGH = "high"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
