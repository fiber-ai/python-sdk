from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_scouting_report_response_200_output_report_media_links_item_type import (
    GetScoutingReportResponse200OutputReportMediaLinksItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportMediaLinksItem")


@_attrs_define
class GetScoutingReportResponse200OutputReportMediaLinksItem:
    """
    Attributes:
        type_ (GetScoutingReportResponse200OutputReportMediaLinksItemType):
        title (str):
        url (str):
        description (None | str | Unset):
    """

    type_: GetScoutingReportResponse200OutputReportMediaLinksItemType
    title: str
    url: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        title = self.title

        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = GetScoutingReportResponse200OutputReportMediaLinksItemType(d.pop("type"))

        title = d.pop("title")

        url = d.pop("url")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        get_scouting_report_response_200_output_report_media_links_item = cls(
            type_=type_,
            title=title,
            url=url,
            description=description,
        )

        get_scouting_report_response_200_output_report_media_links_item.additional_properties = d
        return get_scouting_report_response_200_output_report_media_links_item

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
