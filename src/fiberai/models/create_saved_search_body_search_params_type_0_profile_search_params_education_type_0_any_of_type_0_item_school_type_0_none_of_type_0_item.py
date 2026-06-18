from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0NoneOfType0Item",
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0NoneOfType0Item:
    """Requires at least one identifier: LinkedIn school ID, LinkedIn URL, or website domain to uniquely identify the
    school.

        Attributes:
            linkedin_id (None | str | Unset): The LinkedIn organization ID of the school, like 1646 for Harvard University
            linkedin_url (None | str | Unset): The LinkedIn URL of the school, like
                'https://www.linkedin.com/school/harvard-university/'
            domain (None | str | Unset): The domain of the school, like 'harvard.edu'
    """

    linkedin_id: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_id: None | str | Unset
        if isinstance(self.linkedin_id, Unset):
            linkedin_id = UNSET
        else:
            linkedin_id = self.linkedin_id

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_id is not UNSET:
            field_dict["linkedinId"] = linkedin_id
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_id = _parse_linkedin_id(d.pop("linkedinId", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_none_of_type_0_item = cls(
            linkedin_id=linkedin_id,
            linkedin_url=linkedin_url,
            domain=domain,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_none_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_none_of_type_0_item

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
