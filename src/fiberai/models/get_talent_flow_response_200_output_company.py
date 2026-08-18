from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTalentFlowResponse200OutputCompany")


@_attrs_define
class GetTalentFlowResponse200OutputCompany:
    """Company that was analyzed.

    Attributes:
        name (str): Company name.
        linkedin_org_id (str): LinkedIn organization ID (e.g. '1441' for Google).
        domains (list[str]): Company website domains.
        linkedin_slug (None | str | Unset): LinkedIn company slug (e.g. 'anthropic').
    """

    name: str
    linkedin_org_id: str
    domains: list[str]
    linkedin_slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        linkedin_org_id = self.linkedin_org_id

        domains = self.domains

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "linkedinOrgId": linkedin_org_id,
                "domains": domains,
            }
        )
        if linkedin_slug is not UNSET:
            field_dict["linkedinSlug"] = linkedin_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        linkedin_org_id = d.pop("linkedinOrgId")

        domains = cast(list[str], d.pop("domains"))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug", UNSET))

        get_talent_flow_response_200_output_company = cls(
            name=name,
            linkedin_org_id=linkedin_org_id,
            domains=domains,
            linkedin_slug=linkedin_slug,
        )

        get_talent_flow_response_200_output_company.additional_properties = d
        return get_talent_flow_response_200_output_company

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
