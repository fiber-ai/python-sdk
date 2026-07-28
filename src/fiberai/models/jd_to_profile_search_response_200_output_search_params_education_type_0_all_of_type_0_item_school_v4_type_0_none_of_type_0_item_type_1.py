from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jd_to_profile_search_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v4_type_0_none_of_type_0_item_type_1_identifier import (
    JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0ItemType1Identifier,
)

T = TypeVar(
    "T",
    bound="JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0ItemType1",
)


@_attrs_define
class JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0ItemType1:
    """
    Attributes:
        identifier (JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0It
            emType1Identifier):
        linkedin_url (str):
    """

    identifier: JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0ItemType1Identifier
    linkedin_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier.value

        linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "linkedin_url": linkedin_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = JdToProfileSearchResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV4Type0NoneOfType0ItemType1Identifier(
            d.pop("identifier")
        )

        linkedin_url = d.pop("linkedin_url")

        jd_to_profile_search_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v4_type_0_none_of_type_0_item_type_1 = cls(
            identifier=identifier,
            linkedin_url=linkedin_url,
        )

        jd_to_profile_search_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v4_type_0_none_of_type_0_item_type_1.additional_properties = d
        return jd_to_profile_search_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v4_type_0_none_of_type_0_item_type_1

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
