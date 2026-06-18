from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvestorChange")


@_attrs_define
class InvestorChange:
    """
    Attributes:
        name (str): Investor name
        uuid (None | str): Unique identifier
        type_ (list[str]): Investor types
        linkedin_slug (None | str): Investor LinkedIn profile slug
        crunchbase_url (None | str): Reference URL
    """

    name: str
    uuid: None | str
    type_: list[str]
    linkedin_slug: None | str
    crunchbase_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid: None | str
        uuid = self.uuid

        type_ = self.type_

        linkedin_slug: None | str
        linkedin_slug = self.linkedin_slug

        crunchbase_url: None | str
        crunchbase_url = self.crunchbase_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "type": type_,
                "linkedinSlug": linkedin_slug,
                "crunchbaseUrl": crunchbase_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        type_ = cast(list[str], d.pop("type"))

        def _parse_linkedin_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug"))

        def _parse_crunchbase_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        crunchbase_url = _parse_crunchbase_url(d.pop("crunchbaseUrl"))

        investor_change = cls(
            name=name,
            uuid=uuid,
            type_=type_,
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
