from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacebookGroupDetailsResponse200Output")


@_attrs_define
class FacebookGroupDetailsResponse200Output:
    """
    Attributes:
        id (str): Unique group ID.
        name (str): Group name.
        url (None | str | Unset): URL of the Facebook group.
        description (None | str | Unset): Group description.
        privacy (None | str | Unset): Group privacy (e.g. 'Public' or 'Private').
        member_count (float | None | Unset): Number of members.
    """

    id: str
    name: str
    url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    privacy: None | str | Unset = UNSET
    member_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        privacy: None | str | Unset
        if isinstance(self.privacy, Unset):
            privacy = UNSET
        else:
            privacy = self.privacy

        member_count: float | None | Unset
        if isinstance(self.member_count, Unset):
            member_count = UNSET
        else:
            member_count = self.member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_privacy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy = _parse_privacy(d.pop("privacy", UNSET))

        def _parse_member_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        member_count = _parse_member_count(d.pop("memberCount", UNSET))

        facebook_group_details_response_200_output = cls(
            id=id,
            name=name,
            url=url,
            description=description,
            privacy=privacy,
            member_count=member_count,
        )

        facebook_group_details_response_200_output.additional_properties = d
        return facebook_group_details_response_200_output

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
