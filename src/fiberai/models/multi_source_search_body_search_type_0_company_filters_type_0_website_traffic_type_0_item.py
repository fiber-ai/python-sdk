from enum import StrEnum


class MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item(StrEnum):
    UNKNOWN = "unknown"
    VALUE_0 = "<1K"
    VALUE_1 = "1K-10K"
    VALUE_2 = "10K-100K"
    VALUE_3 = "100K-1M"
    VALUE_4 = "1M+"

    def __str__(self) -> str:
        return str(self.value)
