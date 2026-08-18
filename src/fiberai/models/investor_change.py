from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestorChange")


@_attrs_define
class InvestorChange:
    """
    Attributes:
        name (str): Investor name
        type_ (list[str]): Investor types
        uuid (None | str | Unset): Unique identifier
        linkedin_slug (None | str | Unset): Investor LinkedIn profile slug
        crunchbase_url (None | str | Unset): Reference URL
    """

    name: str
    type_: list[str]
    uuid: None | str | Unset = UNSET
    linkedin_slug: None | str | Unset = UNSET
    crunchbase_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        crunchbase_url: None | str | Unset
        if isinstance(self.crunchbase_url, Unset):
            crunchbase_url = UNSET
        else:
            crunchbase_url = self.crunchbase_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if linkedin_slug is not UNSET:
            field_dict["linkedinSlug"] = linkedin_slug
        if crunchbase_url is not UNSET:
            field_dict["crunchbaseUrl"] = crunchbase_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(list[str], d.pop("type"))

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug", UNSET))

        def _parse_crunchbase_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crunchbase_url = _parse_crunchbase_url(d.pop("crunchbaseUrl", UNSET))

        investor_change = cls(
            name=name,
            type_=type_,
            uuid=uuid,
            linkedin_slug=linkedin_slug,
            crunchbase_url=crunchbase_url,
        )

        investor_change.additional_properties = d
        return investor_change

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
