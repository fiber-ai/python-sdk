from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_body_window_type_1 import FinancialInstrumentLookupBodyWindowType1
from ..models.financial_instrument_lookup_body_window_type_2_type_1 import FinancialInstrumentLookupBodyWindowType2Type1
from ..models.financial_instrument_lookup_body_window_type_3_type_1 import FinancialInstrumentLookupBodyWindowType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_instrument_lookup_body_instrument_type_0 import FinancialInstrumentLookupBodyInstrumentType0
    from ..models.financial_instrument_lookup_body_instrument_type_1 import FinancialInstrumentLookupBodyInstrumentType1
    from ..models.financial_instrument_lookup_body_instrument_type_2 import FinancialInstrumentLookupBodyInstrumentType2
    from ..models.financial_instrument_lookup_body_instrument_type_3 import FinancialInstrumentLookupBodyInstrumentType3
    from ..models.financial_instrument_lookup_body_instrument_type_4 import FinancialInstrumentLookupBodyInstrumentType4


T = TypeVar("T", bound="FinancialInstrumentLookupBody")


@_attrs_define
class FinancialInstrumentLookupBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        instrument (FinancialInstrumentLookupBodyInstrumentType0 | FinancialInstrumentLookupBodyInstrumentType1 |
            FinancialInstrumentLookupBodyInstrumentType2 | FinancialInstrumentLookupBodyInstrumentType3 |
            FinancialInstrumentLookupBodyInstrumentType4): How to identify the instrument. Use `index` for a named market
            index, `mutualFund` for a mutual fund, `stockOrEtf` for a stock or ETF, `currencyPair` for a forex or crypto
            pair, or `customSymbol` for any other format.
        window (FinancialInstrumentLookupBodyWindowType1 | FinancialInstrumentLookupBodyWindowType2Type1 |
            FinancialInstrumentLookupBodyWindowType3Type1 | None | Unset): Time range for the price history graph. Omit for
            `1D` (default, recommended). Setting a non-default window may result in less information being available, so we
            suggest leaving this null unless you have a strong reason not to.
    """

    api_key: str
    instrument: (
        FinancialInstrumentLookupBodyInstrumentType0
        | FinancialInstrumentLookupBodyInstrumentType1
        | FinancialInstrumentLookupBodyInstrumentType2
        | FinancialInstrumentLookupBodyInstrumentType3
        | FinancialInstrumentLookupBodyInstrumentType4
    )
    window: (
        FinancialInstrumentLookupBodyWindowType1
        | FinancialInstrumentLookupBodyWindowType2Type1
        | FinancialInstrumentLookupBodyWindowType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.financial_instrument_lookup_body_instrument_type_0 import (
            FinancialInstrumentLookupBodyInstrumentType0,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_1 import (
            FinancialInstrumentLookupBodyInstrumentType1,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_2 import (
            FinancialInstrumentLookupBodyInstrumentType2,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_3 import (
            FinancialInstrumentLookupBodyInstrumentType3,  # noqa: PLC0415
        )

        api_key = self.api_key

        instrument: dict[str, Any]
        if isinstance(self.instrument, FinancialInstrumentLookupBodyInstrumentType0):
            instrument = self.instrument.to_dict()
        elif isinstance(self.instrument, FinancialInstrumentLookupBodyInstrumentType1):
            instrument = self.instrument.to_dict()
        elif isinstance(self.instrument, FinancialInstrumentLookupBodyInstrumentType2):
            instrument = self.instrument.to_dict()
        elif isinstance(self.instrument, FinancialInstrumentLookupBodyInstrumentType3):
            instrument = self.instrument.to_dict()
        else:
            instrument = self.instrument.to_dict()

        window: None | str | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, FinancialInstrumentLookupBodyWindowType1):
            window = self.window.value
        elif isinstance(self.window, FinancialInstrumentLookupBodyWindowType2Type1):
            window = self.window.value
        elif isinstance(self.window, FinancialInstrumentLookupBodyWindowType3Type1):
            window = self.window.value
        else:
            window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "instrument": instrument,
            }
        )
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_instrument_lookup_body_instrument_type_0 import (
            FinancialInstrumentLookupBodyInstrumentType0,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_1 import (
            FinancialInstrumentLookupBodyInstrumentType1,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_2 import (
            FinancialInstrumentLookupBodyInstrumentType2,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_3 import (
            FinancialInstrumentLookupBodyInstrumentType3,  # noqa: PLC0415
        )
        from ..models.financial_instrument_lookup_body_instrument_type_4 import (
            FinancialInstrumentLookupBodyInstrumentType4,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_instrument(
            data: object,
        ) -> (
            FinancialInstrumentLookupBodyInstrumentType0
            | FinancialInstrumentLookupBodyInstrumentType1
            | FinancialInstrumentLookupBodyInstrumentType2
            | FinancialInstrumentLookupBodyInstrumentType3
            | FinancialInstrumentLookupBodyInstrumentType4
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_0 = FinancialInstrumentLookupBodyInstrumentType0.from_dict(data)

                return instrument_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_1 = FinancialInstrumentLookupBodyInstrumentType1.from_dict(data)

                return instrument_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_2 = FinancialInstrumentLookupBodyInstrumentType2.from_dict(data)

                return instrument_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_3 = FinancialInstrumentLookupBodyInstrumentType3.from_dict(data)

                return instrument_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            instrument_type_4 = FinancialInstrumentLookupBodyInstrumentType4.from_dict(data)

            return instrument_type_4

        instrument = _parse_instrument(d.pop("instrument"))

        def _parse_window(
            data: object,
        ) -> (
            FinancialInstrumentLookupBodyWindowType1
            | FinancialInstrumentLookupBodyWindowType2Type1
            | FinancialInstrumentLookupBodyWindowType3Type1
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
                window_type_1 = FinancialInstrumentLookupBodyWindowType1(data)

                return window_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_type_2_type_1 = FinancialInstrumentLookupBodyWindowType2Type1(data)

                return window_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_type_3_type_1 = FinancialInstrumentLookupBodyWindowType3Type1(data)

                return window_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FinancialInstrumentLookupBodyWindowType1
                | FinancialInstrumentLookupBodyWindowType2Type1
                | FinancialInstrumentLookupBodyWindowType3Type1
                | None
                | Unset,
                data,
            )

        window = _parse_window(d.pop("window", UNSET))

        financial_instrument_lookup_body = cls(
            api_key=api_key,
            instrument=instrument,
            window=window,
        )

        financial_instrument_lookup_body.additional_properties = d
        return financial_instrument_lookup_body

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
