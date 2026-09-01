from enum import StrEnum


class KitchenSinkBulkCompanyResponse200OutputDataItemItemFortuneRankingsType0ItemList(StrEnum):
    FORBES_GLOBAL_2000 = "forbes-global-2000"
    FORTUNE_500_USA = "fortune-500-usa"

    def __str__(self) -> str:
        return str(self.value)
