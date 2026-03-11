from enum import Enum


class TextToCompanySearchResponse200OutputDataItemFundingRoundsType0ItemRoundTypeType2Type1(str, Enum):
    ANGEL = "angel"
    CONVERTIBLE_NOTE = "convertible_note"
    CORPORATE_ROUND = "corporate_round"
    DEBT_FINANCING = "debt_financing"
    EQUITY_CROWDFUNDING = "equity_crowdfunding"
    GRANT = "grant"
    INITIAL_COIN_OFFERING = "initial_coin_offering"
    NON_EQUITY_ASSISTANCE = "non_equity_assistance"
    POST_IPO_DEBT = "post_ipo_debt"
    POST_IPO_EQUITY = "post_ipo_equity"
    POST_IPO_SECONDARY = "post_ipo_secondary"
    PRE_SEED = "pre_seed"
    PRIVATE_EQUITY = "private_equity"
    PRODUCT_CROWDFUNDING = "product_crowdfunding"
    SECONDARY_MARKET = "secondary_market"
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
    SERIES_UNKNOWN = "series_unknown"
    UNDISCLOSED = "undisclosed"

    def __str__(self) -> str:
        return str(self.value)
