from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackedEmployeeChange")


@_attrs_define
class TrackedEmployeeChange:
    """
    Attributes:
        user_id (str): LinkedIn user ID
        name (None | str): Employee name
        title (None | str): Job title
        primary_slug (None | str): LinkedIn profile slug
        linkedin_url (None | str): Full LinkedIn profile URL
        start_date (None | str | Unset): ISO date when the employee started at this company
    """

    user_id: str
    name: None | str
    title: None | str
    primary_slug: None | str
    linkedin_url: None | str
    start_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        name: None | str
        name = self.name

        title: None | str
        title = self.title

        primary_slug: None | str
        primary_slug = self.primary_slug

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "name": name,
                "title": title,
                "primarySlug": primary_slug,
                "linkedinUrl": linkedin_url,
            }
        )
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_primary_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_slug = _parse_primary_slug(d.pop("primarySlug"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        tracked_employee_change = cls(
            user_id=user_id,
            name=name,
            title=title,
            primary_slug=primary_slug,
            linkedin_url=linkedin_url,
            start_date=start_date,
        )

        tracked_employee_change.additional_properties = d
        return tracked_employee_change

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
