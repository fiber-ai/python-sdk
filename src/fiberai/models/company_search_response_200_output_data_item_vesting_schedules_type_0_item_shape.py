from enum import StrEnum


class CompanySearchResponse200OutputDataItemVestingSchedulesType0ItemShape(StrEnum):
    BACKLOADED = "backloaded"
    ERRATIC = "erratic"
    EVEN = "even"
    FRONTLOADED = "frontloaded"

    def __str__(self) -> str:
        return str(self.value)
