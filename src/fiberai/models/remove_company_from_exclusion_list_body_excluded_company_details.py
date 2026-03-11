from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveCompanyFromExclusionListBodyExcludedCompanyDetails")


@_attrs_define
class RemoveCompanyFromExclusionListBodyExcludedCompanyDetails:
    """Details of the companies to remove from the exclusion list

    Attributes:
        domains (list[str] | None | Unset): Domains of the companies to remove from the exclusion list
        linkedin_urls (list[str] | None | Unset): LinkedIn URLs of the companies to remove from the exclusion list
    """

    domains: list[str] | None | Unset = UNSET
    linkedin_urls: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domains: list[str] | None | Unset
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains

        else:
            domains = self.domains

        linkedin_urls: list[str] | None | Unset
        if isinstance(self.linkedin_urls, Unset):
            linkedin_urls = UNSET
        elif isinstance(self.linkedin_urls, list):
            linkedin_urls = self.linkedin_urls

        else:
            linkedin_urls = self.linkedin_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domains is not UNSET:
            field_dict["domains"] = domains
        if linkedin_urls is not UNSET:
            field_dict["linkedinUrls"] = linkedin_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_linkedin_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_urls_type_0 = cast(list[str], data)

                return linkedin_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        linkedin_urls = _parse_linkedin_urls(d.pop("linkedinUrls", UNSET))

        remove_company_from_exclusion_list_body_excluded_company_details = cls(
            domains=domains,
            linkedin_urls=linkedin_urls,
        )

        remove_company_from_exclusion_list_body_excluded_company_details.additional_properties = d
        return remove_company_from_exclusion_list_body_excluded_company_details

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
