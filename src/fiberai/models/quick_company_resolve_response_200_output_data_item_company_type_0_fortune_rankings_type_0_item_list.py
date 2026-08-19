from enum import Enum


class QuickCompanyResolveResponse200OutputDataItemCompanyType0FortuneRankingsType0ItemList(str, Enum):
    FORTUNE_500_USA = "fortune-500-usa"

    def __str__(self) -> str:
        return str(self.value)
