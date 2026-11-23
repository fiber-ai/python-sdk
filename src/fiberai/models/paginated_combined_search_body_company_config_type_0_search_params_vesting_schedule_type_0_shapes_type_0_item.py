from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsVestingScheduleType0ShapesType0Item(StrEnum):
    BACKLOADED = "backloaded"
    ERRATIC = "erratic"
    EVEN = "even"
    FRONTLOADED = "frontloaded"

    def __str__(self) -> str:
        return str(self.value)
