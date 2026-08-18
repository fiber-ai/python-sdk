from enum import Enum


class FinancialInstrumentLookupBodyWindowType3Type1(str, Enum):
    MAX = "MAX"
    VALUE_0 = "1D"
    VALUE_1 = "5D"
    VALUE_2 = "1M"
    VALUE_3 = "6M"
    VALUE_5 = "1Y"
    VALUE_6 = "5Y"
    YTD = "YTD"

    def __str__(self) -> str:
        return str(self.value)
