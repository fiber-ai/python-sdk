from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_tracker_companies_response_200_output_initial_signals_type_0 import (
        AddTrackerCompaniesResponse200OutputInitialSignalsType0,
    )
    from ..models.add_tracker_companies_response_200_output_initial_signals_type_1 import (
        AddTrackerCompaniesResponse200OutputInitialSignalsType1,
    )
    from ..models.add_tracker_companies_response_200_output_invalid_companies_item import (
        AddTrackerCompaniesResponse200OutputInvalidCompaniesItem,
    )


T = TypeVar("T", bound="AddTrackerCompaniesResponse200Output")


@_attrs_define
class AddTrackerCompaniesResponse200Output:
    """
    Attributes:
        added (int): Number of companies successfully added.
        skipped (int): Number skipped (duplicates or invalid).
        invalid_companies (list[AddTrackerCompaniesResponse200OutputInvalidCompaniesItem]): Details on any companies
            that could not be added.
        initial_signals (AddTrackerCompaniesResponse200OutputInitialSignalsType0 |
            AddTrackerCompaniesResponse200OutputInitialSignalsType1): Status of the initial signals request.
    """

    added: int
    skipped: int
    invalid_companies: list[AddTrackerCompaniesResponse200OutputInvalidCompaniesItem]
    initial_signals: (
        AddTrackerCompaniesResponse200OutputInitialSignalsType0
        | AddTrackerCompaniesResponse200OutputInitialSignalsType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_tracker_companies_response_200_output_initial_signals_type_0 import (
            AddTrackerCompaniesResponse200OutputInitialSignalsType0,
        )

        added = self.added

        skipped = self.skipped

        invalid_companies = []
        for invalid_companies_item_data in self.invalid_companies:
            invalid_companies_item = invalid_companies_item_data.to_dict()
            invalid_companies.append(invalid_companies_item)

        initial_signals: dict[str, Any]
        if isinstance(self.initial_signals, AddTrackerCompaniesResponse200OutputInitialSignalsType0):
            initial_signals = self.initial_signals.to_dict()
        else:
            initial_signals = self.initial_signals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "skipped": skipped,
                "invalidCompanies": invalid_companies,
                "initialSignals": initial_signals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_tracker_companies_response_200_output_initial_signals_type_0 import (
            AddTrackerCompaniesResponse200OutputInitialSignalsType0,
        )
        from ..models.add_tracker_companies_response_200_output_initial_signals_type_1 import (
            AddTrackerCompaniesResponse200OutputInitialSignalsType1,
        )
        from ..models.add_tracker_companies_response_200_output_invalid_companies_item import (
            AddTrackerCompaniesResponse200OutputInvalidCompaniesItem,
        )

        d = dict(src_dict)
        added = d.pop("added")

        skipped = d.pop("skipped")

        invalid_companies = []
        _invalid_companies = d.pop("invalidCompanies")
        for invalid_companies_item_data in _invalid_companies:
            invalid_companies_item = AddTrackerCompaniesResponse200OutputInvalidCompaniesItem.from_dict(
                invalid_companies_item_data
            )

            invalid_companies.append(invalid_companies_item)

        def _parse_initial_signals(
            data: object,
        ) -> (
            AddTrackerCompaniesResponse200OutputInitialSignalsType0
            | AddTrackerCompaniesResponse200OutputInitialSignalsType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_signals_type_0 = AddTrackerCompaniesResponse200OutputInitialSignalsType0.from_dict(data)

                return initial_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            initial_signals_type_1 = AddTrackerCompaniesResponse200OutputInitialSignalsType1.from_dict(data)

            return initial_signals_type_1

        initial_signals = _parse_initial_signals(d.pop("initialSignals"))

        add_tracker_companies_response_200_output = cls(
            added=added,
            skipped=skipped,
            invalid_companies=invalid_companies,
            initial_signals=initial_signals,
        )

        add_tracker_companies_response_200_output.additional_properties = d
        return add_tracker_companies_response_200_output

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
