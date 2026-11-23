from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsVestingScheduleType0ShapesType0Item(StrEnum):
    BACKLOADED = "backloaded"
    ERRATIC = "erratic"
    EVEN = "even"
    FRONTLOADED = "frontloaded"

    def __str__(self) -> str:
        return str(self.value)
