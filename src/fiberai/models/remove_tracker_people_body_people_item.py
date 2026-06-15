from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveTrackerPeopleBodyPeopleItem")


@_attrs_define
class RemoveTrackerPeopleBodyPeopleItem:
    """
    Attributes:
        linkedin_url (None | str | Unset): Full LinkedIn profile URL
        linkedin_user_id (None | str | Unset): A person's stable numeric identifier. This is NOT derived from their
            profile URL — retrieve it from a live enrichment lookup. Digits only.
        linkedin_slug (None | str | Unset): The handle in a profile URL — e.g. `williamhgates` in
            https://www.linkedin.com/in/williamhgates/.
    """

    linkedin_url: None | str | Unset = UNSET
    linkedin_user_id: None | str | Unset = UNSET
    linkedin_slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        linkedin_user_id: None | str | Unset
        if isinstance(self.linkedin_user_id, Unset):
            linkedin_user_id = UNSET
        else:
            linkedin_user_id = self.linkedin_user_id

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if linkedin_user_id is not UNSET:
            field_dict["linkedinUserId"] = linkedin_user_id
        if linkedin_slug is not UNSET:
            field_dict["linkedinSlug"] = linkedin_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_linkedin_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_user_id = _parse_linkedin_user_id(d.pop("linkedinUserId", UNSET))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug", UNSET))

        remove_tracker_people_body_people_item = cls(
            linkedin_url=linkedin_url,
            linkedin_user_id=linkedin_user_id,
            linkedin_slug=linkedin_slug,
        )

        remove_tracker_people_body_people_item.additional_properties = d
        return remove_tracker_people_body_people_item

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
