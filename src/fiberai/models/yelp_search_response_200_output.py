from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.yelp_search_response_200_output_businesses_item import YelpSearchResponse200OutputBusinessesItem


T = TypeVar("T", bound="YelpSearchResponse200Output")


@_attrs_define
class YelpSearchResponse200Output:
    """
    Attributes:
        businesses (list[YelpSearchResponse200OutputBusinessesItem]): Matching businesses.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
    """

    businesses: list[YelpSearchResponse200OutputBusinessesItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        businesses = []
        for businesses_item_data in self.businesses:
            businesses_item = businesses_item_data.to_dict()
            businesses.append(businesses_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businesses": businesses,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.yelp_search_response_200_output_businesses_item import (
            YelpSearchResponse200OutputBusinessesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        businesses = []
        _businesses = d.pop("businesses")
        for businesses_item_data in _businesses:
            businesses_item = YelpSearchResponse200OutputBusinessesItem.from_dict(businesses_item_data)

            businesses.append(businesses_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        yelp_search_response_200_output = cls(
            businesses=businesses,
            next_page_token=next_page_token,
        )

        yelp_search_response_200_output.additional_properties = d
        return yelp_search_response_200_output

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
