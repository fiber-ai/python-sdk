from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_statement import (
    FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item import (
        FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item,
    )


T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputFinancialsType0Item")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputFinancialsType0Item:
    """A grouped financial statement with its reporting periods.

    Attributes:
        statement (FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement): Which financial statement
            this group represents.
        periods (list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item] | None | Unset):
            Reporting periods included in this statement.
    """

    statement: FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement
    periods: list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement = self.statement.value

        periods: list[dict[str, Any]] | None | Unset
        if isinstance(self.periods, Unset):
            periods = UNSET
        elif isinstance(self.periods, list):
            periods = []
            for periods_type_0_item_data in self.periods:
                periods_type_0_item = periods_type_0_item_data.to_dict()
                periods.append(periods_type_0_item)

        else:
            periods = self.periods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statement": statement,
            }
        )
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item import (
            FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item,
        )

        d = dict(src_dict)
        statement = FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement(d.pop("statement"))

        def _parse_periods(
            data: object,
        ) -> list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                periods_type_0 = []
                _periods_type_0 = data
                for periods_type_0_item_data in _periods_type_0:
                    periods_type_0_item = (
                        FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item.from_dict(
                            periods_type_0_item_data
                        )
                    )

                    periods_type_0.append(periods_type_0_item)

                return periods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0Item] | None | Unset, data
            )

        periods = _parse_periods(d.pop("periods", UNSET))

        financial_instrument_lookup_response_200_output_financials_type_0_item = cls(
            statement=statement,
            periods=periods,
        )

        financial_instrument_lookup_response_200_output_financials_type_0_item.additional_properties = d
        return financial_instrument_lookup_response_200_output_financials_type_0_item

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
