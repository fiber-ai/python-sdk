from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputNewsType0Item")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputNewsType0Item:
    """A news article related to the instrument.

    Attributes:
        title (None | str | Unset): Article headline.
        url (None | str | Unset): URL of the article.
        source (None | str | Unset): Publisher name.
        published_at (datetime.datetime | None | Unset): ISO 8601 publication timestamp (e.g. '2026-07-28T14:30:00Z').
        is_published_at_estimated (bool | None | Unset): Whether the publishedAt value is an estimate (true) or the
            exact publication timestamp (false). An estimate means only an approximate time like a date or hour was
            available from the source.
        thumbnail_url (None | str | Unset): Thumbnail image URL.
    """

    title: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    is_published_at_estimated: bool | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        is_published_at_estimated: bool | None | Unset
        if isinstance(self.is_published_at_estimated, Unset):
            is_published_at_estimated = UNSET
        else:
            is_published_at_estimated = self.is_published_at_estimated

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if source is not UNSET:
            field_dict["source"] = source
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if is_published_at_estimated is not UNSET:
            field_dict["isPublishedAtEstimated"] = is_published_at_estimated
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_is_published_at_estimated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_published_at_estimated = _parse_is_published_at_estimated(d.pop("isPublishedAtEstimated", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        financial_instrument_lookup_response_200_output_news_type_0_item = cls(
            title=title,
            url=url,
            source=source,
            published_at=published_at,
            is_published_at_estimated=is_published_at_estimated,
            thumbnail_url=thumbnail_url,
        )

        financial_instrument_lookup_response_200_output_news_type_0_item.additional_properties = d
        return financial_instrument_lookup_response_200_output_news_type_0_item

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
