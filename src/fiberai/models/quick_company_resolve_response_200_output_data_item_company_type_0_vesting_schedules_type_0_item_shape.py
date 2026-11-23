from enum import StrEnum


class QuickCompanyResolveResponse200OutputDataItemCompanyType0VestingSchedulesType0ItemShape(StrEnum):
    BACKLOADED = "backloaded"
    ERRATIC = "erratic"
    EVEN = "even"
    FRONTLOADED = "frontloaded"

    def __str__(self) -> str:
        return str(self.value)
