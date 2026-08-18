from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputKeyStatsType0")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputKeyStatsType0:
    """Typed key statistics when available.

    Attributes:
        currency (None | str | Unset): Currency the price-denominated statistics are reported in (e.g. 'USD', 'BTC').
        open_ (float | None | Unset): Opening price for the current session.
        high (float | None | Unset): Session high.
        low (float | None | Unset): Session low.
        market_cap (float | None | Unset): Market capitalization in the instrument's currency. Values from minor-unit
            exchanges are converted to major units.
        average_volume (float | None | Unset): Average trading volume.
        volume (float | None | Unset): Current session volume.
        dividend_yield_percentage (float | None | Unset): Dividend yield as a percentage (e.g. 0.26 for 0.26%).
        pe_ratio (float | None | Unset): Price-to-earnings ratio.
        fifty_two_week_high (float | None | Unset): 52-week high price.
        fifty_two_week_low (float | None | Unset): 52-week low price.
        earnings_per_share (float | None | Unset): Trailing earnings per share (EPS), denominated in the instrument's
            currency. EPS is the portion of a company's profit allocated to each outstanding share — higher values generally
            indicate stronger profitability.
        beta (float | None | Unset): Beta relative to the market: a measure of how volatile the instrument is compared
            to the overall market. Beta > 1 means it tends to amplify market moves; beta < 1 means it tends to be more
            stable.
        shares_outstanding (float | None | Unset): Number of shares outstanding.
    """

    currency: None | str | Unset = UNSET
    open_: float | None | Unset = UNSET
    high: float | None | Unset = UNSET
    low: float | None | Unset = UNSET
    market_cap: float | None | Unset = UNSET
    average_volume: float | None | Unset = UNSET
    volume: float | None | Unset = UNSET
    dividend_yield_percentage: float | None | Unset = UNSET
    pe_ratio: float | None | Unset = UNSET
    fifty_two_week_high: float | None | Unset = UNSET
    fifty_two_week_low: float | None | Unset = UNSET
    earnings_per_share: float | None | Unset = UNSET
    beta: float | None | Unset = UNSET
    shares_outstanding: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        open_: float | None | Unset
        if isinstance(self.open_, Unset):
            open_ = UNSET
        else:
            open_ = self.open_

        high: float | None | Unset
        if isinstance(self.high, Unset):
            high = UNSET
        else:
            high = self.high

        low: float | None | Unset
        if isinstance(self.low, Unset):
            low = UNSET
        else:
            low = self.low

        market_cap: float | None | Unset
        if isinstance(self.market_cap, Unset):
            market_cap = UNSET
        else:
            market_cap = self.market_cap

        average_volume: float | None | Unset
        if isinstance(self.average_volume, Unset):
            average_volume = UNSET
        else:
            average_volume = self.average_volume

        volume: float | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        dividend_yield_percentage: float | None | Unset
        if isinstance(self.dividend_yield_percentage, Unset):
            dividend_yield_percentage = UNSET
        else:
            dividend_yield_percentage = self.dividend_yield_percentage

        pe_ratio: float | None | Unset
        if isinstance(self.pe_ratio, Unset):
            pe_ratio = UNSET
        else:
            pe_ratio = self.pe_ratio

        fifty_two_week_high: float | None | Unset
        if isinstance(self.fifty_two_week_high, Unset):
            fifty_two_week_high = UNSET
        else:
            fifty_two_week_high = self.fifty_two_week_high

        fifty_two_week_low: float | None | Unset
        if isinstance(self.fifty_two_week_low, Unset):
            fifty_two_week_low = UNSET
        else:
            fifty_two_week_low = self.fifty_two_week_low

        earnings_per_share: float | None | Unset
        if isinstance(self.earnings_per_share, Unset):
            earnings_per_share = UNSET
        else:
            earnings_per_share = self.earnings_per_share

        beta: float | None | Unset
        if isinstance(self.beta, Unset):
            beta = UNSET
        else:
            beta = self.beta

        shares_outstanding: float | None | Unset
        if isinstance(self.shares_outstanding, Unset):
            shares_outstanding = UNSET
        else:
            shares_outstanding = self.shares_outstanding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if open_ is not UNSET:
            field_dict["open"] = open_
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if market_cap is not UNSET:
            field_dict["marketCap"] = market_cap
        if average_volume is not UNSET:
            field_dict["averageVolume"] = average_volume
        if volume is not UNSET:
            field_dict["volume"] = volume
        if dividend_yield_percentage is not UNSET:
            field_dict["dividendYieldPercentage"] = dividend_yield_percentage
        if pe_ratio is not UNSET:
            field_dict["peRatio"] = pe_ratio
        if fifty_two_week_high is not UNSET:
            field_dict["fiftyTwoWeekHigh"] = fifty_two_week_high
        if fifty_two_week_low is not UNSET:
            field_dict["fiftyTwoWeekLow"] = fifty_two_week_low
        if earnings_per_share is not UNSET:
            field_dict["earningsPerShare"] = earnings_per_share
        if beta is not UNSET:
            field_dict["beta"] = beta
        if shares_outstanding is not UNSET:
            field_dict["sharesOutstanding"] = shares_outstanding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_open_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        open_ = _parse_open_(d.pop("open", UNSET))

        def _parse_high(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        high = _parse_high(d.pop("high", UNSET))

        def _parse_low(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        low = _parse_low(d.pop("low", UNSET))

        def _parse_market_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_cap = _parse_market_cap(d.pop("marketCap", UNSET))

        def _parse_average_volume(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_volume = _parse_average_volume(d.pop("averageVolume", UNSET))

        def _parse_volume(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        def _parse_dividend_yield_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dividend_yield_percentage = _parse_dividend_yield_percentage(d.pop("dividendYieldPercentage", UNSET))

        def _parse_pe_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ratio = _parse_pe_ratio(d.pop("peRatio", UNSET))

        def _parse_fifty_two_week_high(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fifty_two_week_high = _parse_fifty_two_week_high(d.pop("fiftyTwoWeekHigh", UNSET))

        def _parse_fifty_two_week_low(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fifty_two_week_low = _parse_fifty_two_week_low(d.pop("fiftyTwoWeekLow", UNSET))

        def _parse_earnings_per_share(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        earnings_per_share = _parse_earnings_per_share(d.pop("earningsPerShare", UNSET))

        def _parse_beta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beta = _parse_beta(d.pop("beta", UNSET))

        def _parse_shares_outstanding(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shares_outstanding = _parse_shares_outstanding(d.pop("sharesOutstanding", UNSET))

        financial_instrument_lookup_response_200_output_key_stats_type_0 = cls(
            currency=currency,
            open_=open_,
            high=high,
            low=low,
            market_cap=market_cap,
            average_volume=average_volume,
            volume=volume,
            dividend_yield_percentage=dividend_yield_percentage,
            pe_ratio=pe_ratio,
            fifty_two_week_high=fifty_two_week_high,
            fifty_two_week_low=fifty_two_week_low,
            earnings_per_share=earnings_per_share,
            beta=beta,
            shares_outstanding=shares_outstanding,
        )

        financial_instrument_lookup_response_200_output_key_stats_type_0.additional_properties = d
        return financial_instrument_lookup_response_200_output_key_stats_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
