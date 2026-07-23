from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem")


@_attrs_define
class HotelSearchResponse200OutputPropertiesItemReviewsBreakdownItem:
    """
    Attributes:
        name (None | str | Unset): Review category name.
        description (None | str | Unset): Review category description.
        total_count (int | None | Unset): Total reviews mentioning this category.
        positive_count (int | None | Unset): Positive mentions for this category.
        neutral_count (int | None | Unset): Neutral mentions for this category.
        negative_count (int | None | Unset): Negative mentions for this category.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    total_count: int | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        positive_count: int | None | Unset
        if isinstance(self.positive_count, Unset):
            positive_count = UNSET
        else:
            positive_count = self.positive_count

        neutral_count: int | None | Unset
        if isinstance(self.neutral_count, Unset):
            neutral_count = UNSET
        else:
            neutral_count = self.neutral_count

        negative_count: int | None | Unset
        if isinstance(self.negative_count, Unset):
            negative_count = UNSET
        else:
            negative_count = self.negative_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if positive_count is not UNSET:
            field_dict["positiveCount"] = positive_count
        if neutral_count is not UNSET:
            field_dict["neutralCount"] = neutral_count
        if negative_count is not UNSET:
            field_dict["negativeCount"] = negative_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        def _parse_positive_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        positive_count = _parse_positive_count(d.pop("positiveCount", UNSET))

        def _parse_neutral_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        neutral_count = _parse_neutral_count(d.pop("neutralCount", UNSET))

        def _parse_negative_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        negative_count = _parse_negative_count(d.pop("negativeCount", UNSET))

        hotel_search_response_200_output_properties_item_reviews_breakdown_item = cls(
            name=name,
            description=description,
            total_count=total_count,
            positive_count=positive_count,
            neutral_count=neutral_count,
            negative_count=negative_count,
        )

        hotel_search_response_200_output_properties_item_reviews_breakdown_item.additional_properties = d
        return hotel_search_response_200_output_properties_item_reviews_breakdown_item

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
