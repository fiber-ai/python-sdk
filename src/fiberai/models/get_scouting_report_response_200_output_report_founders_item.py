from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportFoundersItem")


@_attrs_define
class GetScoutingReportResponse200OutputReportFoundersItem:
    """
    Attributes:
        name (str):
        role (None | str | Unset):
        linkedin_url (None | str | Unset):
        profile_pic_url (None | str | Unset):
    """

    name: str
    role: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    profile_pic_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        profile_pic_url: None | str | Unset
        if isinstance(self.profile_pic_url, Unset):
            profile_pic_url = UNSET
        else:
            profile_pic_url = self.profile_pic_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if profile_pic_url is not UNSET:
            field_dict["profilePicUrl"] = profile_pic_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_profile_pic_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_pic_url = _parse_profile_pic_url(d.pop("profilePicUrl", UNSET))

        get_scouting_report_response_200_output_report_founders_item = cls(
            name=name,
            role=role,
            linkedin_url=linkedin_url,
            profile_pic_url=profile_pic_url,
        )

        get_scouting_report_response_200_output_report_founders_item.additional_properties = d
        return get_scouting_report_response_200_output_report_founders_item

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
