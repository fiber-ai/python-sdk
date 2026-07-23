from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_tracker_companies_body_companies_item import AddTrackerCompaniesBodyCompaniesItem
    from ..models.add_tracker_companies_body_initial_signals_type_0 import AddTrackerCompaniesBodyInitialSignalsType0


T = TypeVar("T", bound="AddTrackerCompaniesBody")


@_attrs_define
class AddTrackerCompaniesBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        companies (list[AddTrackerCompaniesBodyCompaniesItem]): Companies to add. At least one identifier required per
            company.
        initial_signals (AddTrackerCompaniesBodyInitialSignalsType0 | None | Unset): When provided, generates signals
            immediately for recent events (funding rounds, news, job postings, social posts) without waiting for the first
            tracking cycle. Only certain rule types support initial signals.
    """

    api_key: str
    companies: list[AddTrackerCompaniesBodyCompaniesItem]
    initial_signals: AddTrackerCompaniesBodyInitialSignalsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_tracker_companies_body_initial_signals_type_0 import (
            AddTrackerCompaniesBodyInitialSignalsType0,
        )

        api_key = self.api_key

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        initial_signals: dict[str, Any] | None | Unset
        if isinstance(self.initial_signals, Unset):
            initial_signals = UNSET
        elif isinstance(self.initial_signals, AddTrackerCompaniesBodyInitialSignalsType0):
            initial_signals = self.initial_signals.to_dict()
        else:
            initial_signals = self.initial_signals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companies": companies,
            }
        )
        if initial_signals is not UNSET:
            field_dict["initialSignals"] = initial_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_tracker_companies_body_companies_item import AddTrackerCompaniesBodyCompaniesItem
        from ..models.add_tracker_companies_body_initial_signals_type_0 import (
            AddTrackerCompaniesBodyInitialSignalsType0,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = AddTrackerCompaniesBodyCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        def _parse_initial_signals(data: object) -> AddTrackerCompaniesBodyInitialSignalsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_signals_type_0 = AddTrackerCompaniesBodyInitialSignalsType0.from_dict(data)

                return initial_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddTrackerCompaniesBodyInitialSignalsType0 | None | Unset, data)

        initial_signals = _parse_initial_signals(d.pop("initialSignals", UNSET))

        add_tracker_companies_body = cls(
            api_key=api_key,
            companies=companies,
            initial_signals=initial_signals,
        )

        add_tracker_companies_body.additional_properties = d
        return add_tracker_companies_body

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
