from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoutingReportResponse200OutputCompany")


@_attrs_define
class GetScoutingReportResponse200OutputCompany:
    """
    Attributes:
        linkedin_url (None | str): LinkedIn company URL. Null when no validated LinkedIn URL could be resolved.
        linkedin_org_id (None | str): LinkedIn numeric organization ID. Null when the company has no known org ID.
        name (None | str): Company display name. Null when the name is not available in our data.
        domain (None | str): Company website domain. Null when the domain is not available in our data.
    """

    linkedin_url: None | str
    linkedin_org_id: None | str
    name: None | str
    domain: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        linkedin_org_id: None | str
        linkedin_org_id = self.linkedin_org_id

        name: None | str
        name = self.name

        domain: None | str
        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "linkedinOrgId": linkedin_org_id,
                "name": name,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_linkedin_org_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_org_id = _parse_linkedin_org_id(d.pop("linkedinOrgId"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain = _parse_domain(d.pop("domain"))

        get_scouting_report_response_200_output_company = cls(
            linkedin_url=linkedin_url,
            linkedin_org_id=linkedin_org_id,
            name=name,
            domain=domain,
        )

        get_scouting_report_response_200_output_company.additional_properties = d
        return get_scouting_report_response_200_output_company

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
