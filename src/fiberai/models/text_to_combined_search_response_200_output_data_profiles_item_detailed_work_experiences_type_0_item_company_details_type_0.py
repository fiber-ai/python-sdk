from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0ItemCompanyDetailsType0",
)


@_attrs_define
class TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0ItemCompanyDetailsType0:
    """
    Attributes:
        linkedin_ids (list[str] | None | Unset):
        li_org_id (None | str | Unset):
        linkedin_primary_slug (None | str | Unset):
        domains (list[str] | None | Unset):
        preferred_name (None | str | Unset):
    """

    linkedin_ids: list[str] | None | Unset = UNSET
    li_org_id: None | str | Unset = UNSET
    linkedin_primary_slug: None | str | Unset = UNSET
    domains: list[str] | None | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_ids: list[str] | None | Unset
        if isinstance(self.linkedin_ids, Unset):
            linkedin_ids = UNSET
        elif isinstance(self.linkedin_ids, list):
            linkedin_ids = self.linkedin_ids

        else:
            linkedin_ids = self.linkedin_ids

        li_org_id: None | str | Unset
        if isinstance(self.li_org_id, Unset):
            li_org_id = UNSET
        else:
            li_org_id = self.li_org_id

        linkedin_primary_slug: None | str | Unset
        if isinstance(self.linkedin_primary_slug, Unset):
            linkedin_primary_slug = UNSET
        else:
            linkedin_primary_slug = self.linkedin_primary_slug

        domains: list[str] | None | Unset
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains

        else:
            domains = self.domains

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_ids is not UNSET:
            field_dict["linkedin_ids"] = linkedin_ids
        if li_org_id is not UNSET:
            field_dict["li_org_id"] = li_org_id
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if domains is not UNSET:
            field_dict["domains"] = domains
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_ids_type_0 = cast(list[str], data)

                return linkedin_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        linkedin_ids = _parse_linkedin_ids(d.pop("linkedin_ids", UNSET))

        def _parse_li_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        li_org_id = _parse_li_org_id(d.pop("li_org_id", UNSET))

        def _parse_linkedin_primary_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_primary_slug = _parse_linkedin_primary_slug(d.pop("linkedin_primary_slug", UNSET))

        def _parse_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        domains = _parse_domains(d.pop("domains", UNSET))

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        text_to_combined_search_response_200_output_data_profiles_item_detailed_work_experiences_type_0_item_company_details_type_0 = cls(
            linkedin_ids=linkedin_ids,
            li_org_id=li_org_id,
            linkedin_primary_slug=linkedin_primary_slug,
            domains=domains,
            preferred_name=preferred_name,
        )

        text_to_combined_search_response_200_output_data_profiles_item_detailed_work_experiences_type_0_item_company_details_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_data_profiles_item_detailed_work_experiences_type_0_item_company_details_type_0

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
