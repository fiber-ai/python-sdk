from enum import Enum


class MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item(str, Enum):
    DECLINING = "declining"
    GROWING = "growing"
    HIGH = "high"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
