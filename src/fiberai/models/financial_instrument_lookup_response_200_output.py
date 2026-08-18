from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_instrument_lookup_response_200_output_company_info_type_0 import (
        FinancialInstrumentLookupResponse200OutputCompanyInfoType0,
    )
    from ..models.financial_instrument_lookup_response_200_output_extended_hours_quote_type_0 import (
        FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0,
    )
    from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item import (
        FinancialInstrumentLookupResponse200OutputFinancialsType0Item,
    )
    from ..models.financial_instrument_lookup_response_200_output_instrument_type_0 import (
        FinancialInstrumentLookupResponse200OutputInstrumentType0,
    )
    from ..models.financial_instrument_lookup_response_200_output_key_stats_type_0 import (
        FinancialInstrumentLookupResponse200OutputKeyStatsType0,
    )
    from ..models.financial_instrument_lookup_response_200_output_news_type_0_item import (
        FinancialInstrumentLookupResponse200OutputNewsType0Item,
    )
    from ..models.financial_instrument_lookup_response_200_output_price_history_type_0_item import (
        FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item,
    )
    from ..models.financial_instrument_lookup_response_200_output_quote_type_0 import (
        FinancialInstrumentLookupResponse200OutputQuoteType0,
    )


T = TypeVar("T", bound="FinancialInstrumentLookupResponse200Output")


@_attrs_define
class FinancialInstrumentLookupResponse200Output:
    """
    Attributes:
        instrument (FinancialInstrumentLookupResponse200OutputInstrumentType0 | None | Unset): Core identity of the
            looked-up instrument.
        quote (FinancialInstrumentLookupResponse200OutputQuoteType0 | None | Unset): Latest regular-session quote.
        extended_hours_quote (FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0 | None | Unset):
            Extended-hours (pre/post-market) quote when reported separately.
        key_stats (FinancialInstrumentLookupResponse200OutputKeyStatsType0 | None | Unset): Typed key statistics when
            available.
        company_info (FinancialInstrumentLookupResponse200OutputCompanyInfoType0 | None | Unset): Company information
            when available — description, leadership, sector, headquarters, etc.
        financials (list[FinancialInstrumentLookupResponse200OutputFinancialsType0Item] | None | Unset): Quarterly and
            annual financial statements when available.
        news (list[FinancialInstrumentLookupResponse200OutputNewsType0Item] | None | Unset): Recent news articles
            related to the instrument.
        price_history (list[FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item] | None | Unset): Recent
            price history for the instrument.
    """

    instrument: FinancialInstrumentLookupResponse200OutputInstrumentType0 | None | Unset = UNSET
    quote: FinancialInstrumentLookupResponse200OutputQuoteType0 | None | Unset = UNSET
    extended_hours_quote: FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0 | None | Unset = UNSET
    key_stats: FinancialInstrumentLookupResponse200OutputKeyStatsType0 | None | Unset = UNSET
    company_info: FinancialInstrumentLookupResponse200OutputCompanyInfoType0 | None | Unset = UNSET
    financials: list[FinancialInstrumentLookupResponse200OutputFinancialsType0Item] | None | Unset = UNSET
    news: list[FinancialInstrumentLookupResponse200OutputNewsType0Item] | None | Unset = UNSET
    price_history: list[FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.financial_instrument_lookup_response_200_output_company_info_type_0 import (
            FinancialInstrumentLookupResponse200OutputCompanyInfoType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_extended_hours_quote_type_0 import (
            FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_instrument_type_0 import (
            FinancialInstrumentLookupResponse200OutputInstrumentType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_key_stats_type_0 import (
            FinancialInstrumentLookupResponse200OutputKeyStatsType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_quote_type_0 import (
            FinancialInstrumentLookupResponse200OutputQuoteType0,
        )

        instrument: dict[str, Any] | None | Unset
        if isinstance(self.instrument, Unset):
            instrument = UNSET
        elif isinstance(self.instrument, FinancialInstrumentLookupResponse200OutputInstrumentType0):
            instrument = self.instrument.to_dict()
        else:
            instrument = self.instrument

        quote: dict[str, Any] | None | Unset
        if isinstance(self.quote, Unset):
            quote = UNSET
        elif isinstance(self.quote, FinancialInstrumentLookupResponse200OutputQuoteType0):
            quote = self.quote.to_dict()
        else:
            quote = self.quote

        extended_hours_quote: dict[str, Any] | None | Unset
        if isinstance(self.extended_hours_quote, Unset):
            extended_hours_quote = UNSET
        elif isinstance(self.extended_hours_quote, FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0):
            extended_hours_quote = self.extended_hours_quote.to_dict()
        else:
            extended_hours_quote = self.extended_hours_quote

        key_stats: dict[str, Any] | None | Unset
        if isinstance(self.key_stats, Unset):
            key_stats = UNSET
        elif isinstance(self.key_stats, FinancialInstrumentLookupResponse200OutputKeyStatsType0):
            key_stats = self.key_stats.to_dict()
        else:
            key_stats = self.key_stats

        company_info: dict[str, Any] | None | Unset
        if isinstance(self.company_info, Unset):
            company_info = UNSET
        elif isinstance(self.company_info, FinancialInstrumentLookupResponse200OutputCompanyInfoType0):
            company_info = self.company_info.to_dict()
        else:
            company_info = self.company_info

        financials: list[dict[str, Any]] | None | Unset
        if isinstance(self.financials, Unset):
            financials = UNSET
        elif isinstance(self.financials, list):
            financials = []
            for financials_type_0_item_data in self.financials:
                financials_type_0_item = financials_type_0_item_data.to_dict()
                financials.append(financials_type_0_item)

        else:
            financials = self.financials

        news: list[dict[str, Any]] | None | Unset
        if isinstance(self.news, Unset):
            news = UNSET
        elif isinstance(self.news, list):
            news = []
            for news_type_0_item_data in self.news:
                news_type_0_item = news_type_0_item_data.to_dict()
                news.append(news_type_0_item)

        else:
            news = self.news

        price_history: list[dict[str, Any]] | None | Unset
        if isinstance(self.price_history, Unset):
            price_history = UNSET
        elif isinstance(self.price_history, list):
            price_history = []
            for price_history_type_0_item_data in self.price_history:
                price_history_type_0_item = price_history_type_0_item_data.to_dict()
                price_history.append(price_history_type_0_item)

        else:
            price_history = self.price_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if quote is not UNSET:
            field_dict["quote"] = quote
        if extended_hours_quote is not UNSET:
            field_dict["extendedHoursQuote"] = extended_hours_quote
        if key_stats is not UNSET:
            field_dict["keyStats"] = key_stats
        if company_info is not UNSET:
            field_dict["companyInfo"] = company_info
        if financials is not UNSET:
            field_dict["financials"] = financials
        if news is not UNSET:
            field_dict["news"] = news
        if price_history is not UNSET:
            field_dict["priceHistory"] = price_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_instrument_lookup_response_200_output_company_info_type_0 import (
            FinancialInstrumentLookupResponse200OutputCompanyInfoType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_extended_hours_quote_type_0 import (
            FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item import (
            FinancialInstrumentLookupResponse200OutputFinancialsType0Item,
        )
        from ..models.financial_instrument_lookup_response_200_output_instrument_type_0 import (
            FinancialInstrumentLookupResponse200OutputInstrumentType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_key_stats_type_0 import (
            FinancialInstrumentLookupResponse200OutputKeyStatsType0,
        )
        from ..models.financial_instrument_lookup_response_200_output_news_type_0_item import (
            FinancialInstrumentLookupResponse200OutputNewsType0Item,
        )
        from ..models.financial_instrument_lookup_response_200_output_price_history_type_0_item import (
            FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item,
        )
        from ..models.financial_instrument_lookup_response_200_output_quote_type_0 import (
            FinancialInstrumentLookupResponse200OutputQuoteType0,
        )

        d = dict(src_dict)

        def _parse_instrument(data: object) -> FinancialInstrumentLookupResponse200OutputInstrumentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_0 = FinancialInstrumentLookupResponse200OutputInstrumentType0.from_dict(data)

                return instrument_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputInstrumentType0 | None | Unset, data)

        instrument = _parse_instrument(d.pop("instrument", UNSET))

        def _parse_quote(data: object) -> FinancialInstrumentLookupResponse200OutputQuoteType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quote_type_0 = FinancialInstrumentLookupResponse200OutputQuoteType0.from_dict(data)

                return quote_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputQuoteType0 | None | Unset, data)

        quote = _parse_quote(d.pop("quote", UNSET))

        def _parse_extended_hours_quote(
            data: object,
        ) -> FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extended_hours_quote_type_0 = (
                    FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0.from_dict(data)
                )

                return extended_hours_quote_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0 | None | Unset, data)

        extended_hours_quote = _parse_extended_hours_quote(d.pop("extendedHoursQuote", UNSET))

        def _parse_key_stats(data: object) -> FinancialInstrumentLookupResponse200OutputKeyStatsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_stats_type_0 = FinancialInstrumentLookupResponse200OutputKeyStatsType0.from_dict(data)

                return key_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputKeyStatsType0 | None | Unset, data)

        key_stats = _parse_key_stats(d.pop("keyStats", UNSET))

        def _parse_company_info(
            data: object,
        ) -> FinancialInstrumentLookupResponse200OutputCompanyInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_info_type_0 = FinancialInstrumentLookupResponse200OutputCompanyInfoType0.from_dict(data)

                return company_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputCompanyInfoType0 | None | Unset, data)

        company_info = _parse_company_info(d.pop("companyInfo", UNSET))

        def _parse_financials(
            data: object,
        ) -> list[FinancialInstrumentLookupResponse200OutputFinancialsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                financials_type_0 = []
                _financials_type_0 = data
                for financials_type_0_item_data in _financials_type_0:
                    financials_type_0_item = FinancialInstrumentLookupResponse200OutputFinancialsType0Item.from_dict(
                        financials_type_0_item_data
                    )

                    financials_type_0.append(financials_type_0_item)

                return financials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FinancialInstrumentLookupResponse200OutputFinancialsType0Item] | None | Unset, data)

        financials = _parse_financials(d.pop("financials", UNSET))

        def _parse_news(data: object) -> list[FinancialInstrumentLookupResponse200OutputNewsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                news_type_0 = []
                _news_type_0 = data
                for news_type_0_item_data in _news_type_0:
                    news_type_0_item = FinancialInstrumentLookupResponse200OutputNewsType0Item.from_dict(
                        news_type_0_item_data
                    )

                    news_type_0.append(news_type_0_item)

                return news_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FinancialInstrumentLookupResponse200OutputNewsType0Item] | None | Unset, data)

        news = _parse_news(d.pop("news", UNSET))

        def _parse_price_history(
            data: object,
        ) -> list[FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                price_history_type_0 = []
                _price_history_type_0 = data
                for price_history_type_0_item_data in _price_history_type_0:
                    price_history_type_0_item = (
                        FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item.from_dict(
                            price_history_type_0_item_data
                        )
                    )

                    price_history_type_0.append(price_history_type_0_item)

                return price_history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item] | None | Unset, data)

        price_history = _parse_price_history(d.pop("priceHistory", UNSET))

        financial_instrument_lookup_response_200_output = cls(
            instrument=instrument,
            quote=quote,
            extended_hours_quote=extended_hours_quote,
            key_stats=key_stats,
            company_info=company_info,
            financials=financials,
            news=news,
            price_history=price_history,
        )

        financial_instrument_lookup_response_200_output.additional_properties = d
        return financial_instrument_lookup_response_200_output

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
