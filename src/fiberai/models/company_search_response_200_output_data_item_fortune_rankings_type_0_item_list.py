from enum import StrEnum


class CompanySearchResponse200OutputDataItemFortuneRankingsType0ItemList(StrEnum):
    FORTUNE_500_USA = "fortune-500-usa"

    def __str__(self) -> str:
        return str(self.value)
