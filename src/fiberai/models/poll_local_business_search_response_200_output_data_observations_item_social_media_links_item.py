from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem:
    """
    Attributes:
        url (str):
        platform (str):
    """

    url: str
    platform: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "platform": platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        platform = d.pop("platform")

        poll_local_business_search_response_200_output_data_observations_item_social_media_links_item = cls(
            url=url,
            platform=platform,
        )

        poll_local_business_search_response_200_output_data_observations_item_social_media_links_item.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_social_media_links_item

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
