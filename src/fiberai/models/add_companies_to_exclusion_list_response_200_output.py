from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_companies_to_exclusion_list_response_200_output_invalid_identifiers_item import (
        AddCompaniesToExclusionListResponse200OutputInvalidIdentifiersItem,
    )


T = TypeVar("T", bound="AddCompaniesToExclusionListResponse200Output")


@_attrs_define
class AddCompaniesToExclusionListResponse200Output:
    """
    Attributes:
        list_id (str): The ID of the company exclusion list.
        companies_added (float): Number of companies added to the exclusion list
        invalid_identifiers (list[AddCompaniesToExclusionListResponse200OutputInvalidIdentifiersItem]): Entries that
            could not be added because they had no valid company domain or LinkedIn company URL. Valid entries in the same
            request are still added.
    """

    list_id: str
    companies_added: float
    invalid_identifiers: list[AddCompaniesToExclusionListResponse200OutputInvalidIdentifiersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        companies_added = self.companies_added

        invalid_identifiers = []
        for invalid_identifiers_item_data in self.invalid_identifiers:
            invalid_identifiers_item = invalid_identifiers_item_data.to_dict()
            invalid_identifiers.append(invalid_identifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "companiesAdded": companies_added,
                "invalidIdentifiers": invalid_identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_companies_to_exclusion_list_response_200_output_invalid_identifiers_item import (
            AddCompaniesToExclusionListResponse200OutputInvalidIdentifiersItem,
        )

        d = dict(src_dict)
        list_id = d.pop("listId")

        companies_added = d.pop("companiesAdded")

        invalid_identifiers = []
        _invalid_identifiers = d.pop("invalidIdentifiers")
        for invalid_identifiers_item_data in _invalid_identifiers:
            invalid_identifiers_item = AddCompaniesToExclusionListResponse200OutputInvalidIdentifiersItem.from_dict(
                invalid_identifiers_item_data
            )

            invalid_identifiers.append(invalid_identifiers_item)

        add_companies_to_exclusion_list_response_200_output = cls(
            list_id=list_id,
            companies_added=companies_added,
            invalid_identifiers=invalid_identifiers,
        )

        add_companies_to_exclusion_list_response_200_output.additional_properties = d
        return add_companies_to_exclusion_list_response_200_output

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
