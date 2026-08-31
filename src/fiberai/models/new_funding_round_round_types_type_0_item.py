from enum import StrEnum


class NewFundingRoundRoundTypesType0Item(StrEnum):
    ANGEL = "angel"
    CONVERTIBLE_NOTE = "convertible_note"
    CORPORATE_ROUND = "corporate_round"
    DEBT_FINANCING = "debt_financing"
    GRANT = "grant"
    PRE_SEED = "pre_seed"
    PRIVATE_EQUITY = "private_equity"
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    SERIES_D = "series_d"
    SERIES_E = "series_e"
    SERIES_F = "series_f"
    SERIES_G = "series_g"
    UNDISCLOSED = "undisclosed"

    def __str__(self) -> str:
        return str(self.value)
