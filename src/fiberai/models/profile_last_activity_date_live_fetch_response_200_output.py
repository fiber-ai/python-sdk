from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileLastActivityDateLiveFetchResponse200Output")


@_attrs_define
class ProfileLastActivityDateLiveFetchResponse200Output:
    """
    Attributes:
        last_activity_at (None | str | Unset): Timestamp of the most recent public LinkedIn activity (post, comment,
            reaction, share, or repost) in ISO 8601 format, or null when no activity is available. This is not a 'last
            login' or 'last seen online' value.
    """

    last_activity_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = self.last_activity_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_last_activity_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))

        profile_last_activity_date_live_fetch_response_200_output = cls(
            last_activity_at=last_activity_at,
        )

        profile_last_activity_date_live_fetch_response_200_output.additional_properties = d
        return profile_last_activity_date_live_fetch_response_200_output

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
