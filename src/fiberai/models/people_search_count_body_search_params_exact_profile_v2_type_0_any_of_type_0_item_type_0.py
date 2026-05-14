from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_count_body_search_params_exact_profile_v2_type_0_any_of_type_0_item_type_0_identifier import (
    PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0Identifier,
)

T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0:
    """
    Attributes:
        identifier (PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0Identifier):
        linkedin_slug (str):
    """

    identifier: PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0Identifier
    linkedin_slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        linkedin_slug = self.linkedin_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "linkedin_slug": linkedin_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = PeopleSearchCountBodySearchParamsExactProfileV2Type0AnyOfType0ItemType0Identifier(
            d.pop("identifier")
        )

        linkedin_slug = d.pop("linkedin_slug")

        people_search_count_body_search_params_exact_profile_v2_type_0_any_of_type_0_item_type_0 = cls(
            identifier=identifier,
            linkedin_slug=linkedin_slug,
        )

        people_search_count_body_search_params_exact_profile_v2_type_0_any_of_type_0_item_type_0.additional_properties = d
        return people_search_count_body_search_params_exact_profile_v2_type_0_any_of_type_0_item_type_0

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
