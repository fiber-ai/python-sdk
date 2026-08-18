from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType0Index(str, Enum):
    DOW_JONES = "DOW_JONES"
    FTSE_100 = "FTSE_100"
    NASDAQ_100 = "NASDAQ_100"
    NASDAQ_COMPOSITE = "NASDAQ_COMPOSITE"
    RUSSELL_1000 = "RUSSELL_1000"
    RUSSELL_2000 = "RUSSELL_2000"
    RUSSELL_3000 = "RUSSELL_3000"
    SP_500 = "SP_500"

    def __str__(self) -> str:
        return str(self.value)
