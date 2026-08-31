from enum import StrEnum


class MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item(StrEnum):
    DECLINING = "declining"
    GROWING = "growing"
    HIGH = "high"
    STABLE = "stable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
