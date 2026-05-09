from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webpage_screenshot_response_200_output_image_media_type import (
    WebpageScreenshotResponse200OutputImageMediaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebpageScreenshotResponse200Output")


@_attrs_define
class WebpageScreenshotResponse200Output:
    """
    Attributes:
        screenshot_url (str): Hosted URL of the captured screenshot image in PNG format.
        page_url (str): The final URL of the page that was screenshotted, after following any redirects. May differ from
            the input URL if the page redirects.
        image_media_type (WebpageScreenshotResponse200OutputImageMediaType): MIME type of the screenshot image.
        captured_at (str): ISO 8601 timestamp of when the screenshot was captured.
        page_title (None | str | Unset): The HTML title of the screenshotted page, if available.
    """

    screenshot_url: str
    page_url: str
    image_media_type: WebpageScreenshotResponse200OutputImageMediaType
    captured_at: str
    page_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        screenshot_url = self.screenshot_url

        page_url = self.page_url

        image_media_type = self.image_media_type.value

        captured_at = self.captured_at

        page_title: None | str | Unset
        if isinstance(self.page_title, Unset):
            page_title = UNSET
        else:
            page_title = self.page_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "screenshotUrl": screenshot_url,
                "pageUrl": page_url,
                "imageMediaType": image_media_type,
                "capturedAt": captured_at,
            }
        )
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        screenshot_url = d.pop("screenshotUrl")

        page_url = d.pop("pageUrl")

        image_media_type = WebpageScreenshotResponse200OutputImageMediaType(d.pop("imageMediaType"))

        captured_at = d.pop("capturedAt")

        def _parse_page_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_title = _parse_page_title(d.pop("pageTitle", UNSET))

        webpage_screenshot_response_200_output = cls(
            screenshot_url=screenshot_url,
            page_url=page_url,
            image_media_type=image_media_type,
            captured_at=captured_at,
            page_title=page_title,
        )

        webpage_screenshot_response_200_output.additional_properties = d
        return webpage_screenshot_response_200_output

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
