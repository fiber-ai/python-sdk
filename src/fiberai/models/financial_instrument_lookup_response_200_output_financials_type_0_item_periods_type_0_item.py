from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_period_type_type_1 import (
    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1,
)
from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_period_type_type_2_type_1 import (
    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1,
)
from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_period_type_type_3_type_1 import (
    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_line_items_type_0_item import (
        FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item,
    )


T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item:
    """One reporting period of statement data.

    Attributes:
        period_end_date (None | str | Unset): Calendar date the reporting period ended, as YYYY-MM-DD. Null when only a
            year or a quarter number is available, since the period's end depends on the company's fiscal calendar.
        period_label (None | str | Unset): Period label such as 'Jun 2026', 'Q2 2026', or '2025'. Use periodEndDate to
            order or compare periods; a label may follow either the calendar year or the company's own fiscal year.
        period_type (FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1 |
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1 |
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1 | None |
            Unset): Whether the period is quarterly or annual.
        currency (None | str | Unset): Currency of the reported values.
        line_items
            (list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item] | None |
            Unset): Line items reported for this period.
    """

    period_end_date: None | str | Unset = UNSET
    period_label: None | str | Unset = UNSET
    period_type: (
        FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1
        | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1
        | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1
        | None
        | Unset
    ) = UNSET
    currency: None | str | Unset = UNSET
    line_items: (
        list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_end_date: None | str | Unset
        if isinstance(self.period_end_date, Unset):
            period_end_date = UNSET
        else:
            period_end_date = self.period_end_date

        period_label: None | str | Unset
        if isinstance(self.period_label, Unset):
            period_label = UNSET
        else:
            period_label = self.period_label

        period_type: None | str | Unset
        if isinstance(self.period_type, Unset):
            period_type = UNSET
        elif isinstance(
            self.period_type,
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1,
        ):
            period_type = self.period_type.value
        elif isinstance(
            self.period_type,
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1,
        ):
            period_type = self.period_type.value
        elif isinstance(
            self.period_type,
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1,
        ):
            period_type = self.period_type.value
        else:
            period_type = self.period_type

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        line_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.line_items, Unset):
            line_items = UNSET
        elif isinstance(self.line_items, list):
            line_items = []
            for line_items_type_0_item_data in self.line_items:
                line_items_type_0_item = line_items_type_0_item_data.to_dict()
                line_items.append(line_items_type_0_item)

        else:
            line_items = self.line_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_end_date is not UNSET:
            field_dict["periodEndDate"] = period_end_date
        if period_label is not UNSET:
            field_dict["periodLabel"] = period_label
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_line_items_type_0_item import (
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item,
        )

        d = dict(src_dict)

        def _parse_period_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_end_date = _parse_period_end_date(d.pop("periodEndDate", UNSET))

        def _parse_period_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_label = _parse_period_label(d.pop("periodLabel", UNSET))

        def _parse_period_type(
            data: object,
        ) -> (
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1
            | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1
            | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_type_1 = (
                    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1(data)
                )

                return period_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_type_2_type_1 = (
                    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1(
                        data
                    )
                )

                return period_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_type_3_type_1 = (
                    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1(
                        data
                    )
                )

                return period_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType1
                | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType2Type1
                | FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1
                | None
                | Unset,
                data,
            )

        period_type = _parse_period_type(d.pop("periodType", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_line_items(
            data: object,
        ) -> (
            list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                line_items_type_0 = []
                _line_items_type_0 = data
                for line_items_type_0_item_data in _line_items_type_0:
                    line_items_type_0_item = FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item.from_dict(
                        line_items_type_0_item_data
                    )

                    line_items_type_0.append(line_items_type_0_item)

                return line_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item]
                | None
                | Unset,
                data,
            )

        line_items = _parse_line_items(d.pop("lineItems", UNSET))

        financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item = cls(
            period_end_date=period_end_date,
            period_label=period_label,
            period_type=period_type,
            currency=currency,
            line_items=line_items,
        )

        financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item.additional_properties = d
        return financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item

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
