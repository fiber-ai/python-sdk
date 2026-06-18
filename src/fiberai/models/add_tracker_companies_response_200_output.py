from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
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
    """

    added: int
    skipped: int
    invalid_companies: list[AddTrackerCompaniesResponse200OutputInvalidCompaniesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        skipped = self.skipped

        invalid_companies = []
        for invalid_companies_item_data in self.invalid_companies:
            invalid_companies_item = invalid_companies_item_data.to_dict()
            invalid_companies.append(invalid_companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "skipped": skipped,
                "invalidCompanies": invalid_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        add_tracker_companies_response_200_output = cls(
            added=added,
            skipped=skipped,
            invalid_companies=invalid_companies,
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
