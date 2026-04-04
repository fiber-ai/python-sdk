from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportBlogPostsItem")


@_attrs_define
class GetScoutingReportResponse200OutputReportBlogPostsItem:
    """
    Attributes:
        title (str):
        url (str):
        date (None | str | Unset):
        summary (None | str | Unset):
    """

    title: str
    url: str
    date: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "url": url,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        url = d.pop("url")

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        get_scouting_report_response_200_output_report_blog_posts_item = cls(
            title=title,
            url=url,
            date=date,
            summary=summary,
        )

        get_scouting_report_response_200_output_report_blog_posts_item.additional_properties = d
        return get_scouting_report_response_200_output_report_blog_posts_item

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
