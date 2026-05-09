from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webpage_screenshot_body_format import WebpageScreenshotBodyFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebpageScreenshotBody")


@_attrs_define
class WebpageScreenshotBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        url (str): The URL of the webpage to capture (e.g. 'https://stripe.com/pricing'). Bare domains like 'stripe.com'
            are also accepted and will be treated as HTTPS.
        full_page (bool | Unset): If true, captures the entire scrollable page. Defaults to false (viewport only).
            Default: False.
        format_ (WebpageScreenshotBodyFormat | Unset): Device format for the capture. 'mobile' uses a phone-sized
            viewport, 'desktop' uses a standard widescreen viewport. Defaults to 'desktop'. Default:
            WebpageScreenshotBodyFormat.DESKTOP.
        country (None | str | Unset): ISO 3166-1 alpha-3 country code for geo-located capture (e.g. 'USA', 'GBR',
            'DEU'). If omitted, defaults to a US-based capture.
    """

    api_key: str
    url: str
    full_page: bool | Unset = False
    format_: WebpageScreenshotBodyFormat | Unset = WebpageScreenshotBodyFormat.DESKTOP
    country: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        url = self.url

        full_page = self.full_page

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "url": url,
            }
        )
        if full_page is not UNSET:
            field_dict["fullPage"] = full_page
        if format_ is not UNSET:
            field_dict["format"] = format_
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        url = d.pop("url")

        full_page = d.pop("fullPage", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: WebpageScreenshotBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = WebpageScreenshotBodyFormat(_format_)

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        webpage_screenshot_body = cls(
            api_key=api_key,
            url=url,
            full_page=full_page,
            format_=format_,
            country=country,
        )

        webpage_screenshot_body.additional_properties = d
        return webpage_screenshot_body

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
