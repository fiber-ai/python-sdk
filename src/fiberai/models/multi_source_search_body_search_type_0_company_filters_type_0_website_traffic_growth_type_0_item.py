from enum import Enum


class MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item(str, Enum):
    DECLINING = "declining"
    GROWING = "growing"
    HIGH = "high"
    STABLE = "stable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
