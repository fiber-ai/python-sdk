from enum import StrEnum


class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyVestingSchedulesType0ItemShape(StrEnum):
    BACKLOADED = "backloaded"
    ERRATIC = "erratic"
    EVEN = "even"
    FRONTLOADED = "frontloaded"

    def __str__(self) -> str:
        return str(self.value)
