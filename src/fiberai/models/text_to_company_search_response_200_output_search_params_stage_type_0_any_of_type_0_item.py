from enum import Enum


class TextToCompanySearchResponse200OutputSearchParamsStageType0AnyOfType0Item(str, Enum):
    ACQUIRED = "acquired"
    CLOSED = "closed"
    NO_FUNDING_YET = "no_funding_yet"
    PRE_SEED = "pre_seed"
    PRIVATE_EQUITY = "private_equity"
    PUBLIC = "public"
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    SERIES_D = "series_d"
    SERIES_E = "series_e"
    SERIES_F = "series_f"
    SERIES_G = "series_g"
    SERIES_H = "series_h"
    SERIES_I = "series_i"
    SERIES_J = "series_j"
    UNKNOWN = "unknown"
    VENTURE_OTHER = "venture_other"

    def __str__(self) -> str:
        return str(self.value)
