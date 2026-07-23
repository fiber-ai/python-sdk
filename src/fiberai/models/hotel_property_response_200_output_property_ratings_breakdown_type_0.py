from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelPropertyResponse200OutputPropertyRatingsBreakdownType0")


@_attrs_define
class HotelPropertyResponse200OutputPropertyRatingsBreakdownType0:
    """Guest review counts grouped by one- through five-star rating.

    Attributes:
        one_star_count (int | None | Unset): Count of 1-star reviews.
        two_star_count (int | None | Unset): Count of 2-star reviews.
        three_star_count (int | None | Unset): Count of 3-star reviews.
        four_star_count (int | None | Unset): Count of 4-star reviews.
        five_star_count (int | None | Unset): Count of 5-star reviews.
    """

    one_star_count: int | None | Unset = UNSET
    two_star_count: int | None | Unset = UNSET
    three_star_count: int | None | Unset = UNSET
    four_star_count: int | None | Unset = UNSET
    five_star_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_star_count: int | None | Unset
        if isinstance(self.one_star_count, Unset):
            one_star_count = UNSET
        else:
            one_star_count = self.one_star_count

        two_star_count: int | None | Unset
        if isinstance(self.two_star_count, Unset):
            two_star_count = UNSET
        else:
            two_star_count = self.two_star_count

        three_star_count: int | None | Unset
        if isinstance(self.three_star_count, Unset):
            three_star_count = UNSET
        else:
            three_star_count = self.three_star_count

        four_star_count: int | None | Unset
        if isinstance(self.four_star_count, Unset):
            four_star_count = UNSET
        else:
            four_star_count = self.four_star_count

        five_star_count: int | None | Unset
        if isinstance(self.five_star_count, Unset):
            five_star_count = UNSET
        else:
            five_star_count = self.five_star_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if one_star_count is not UNSET:
            field_dict["oneStarCount"] = one_star_count
        if two_star_count is not UNSET:
            field_dict["twoStarCount"] = two_star_count
        if three_star_count is not UNSET:
            field_dict["threeStarCount"] = three_star_count
        if four_star_count is not UNSET:
            field_dict["fourStarCount"] = four_star_count
        if five_star_count is not UNSET:
            field_dict["fiveStarCount"] = five_star_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_one_star_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        one_star_count = _parse_one_star_count(d.pop("oneStarCount", UNSET))

        def _parse_two_star_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        two_star_count = _parse_two_star_count(d.pop("twoStarCount", UNSET))

        def _parse_three_star_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        three_star_count = _parse_three_star_count(d.pop("threeStarCount", UNSET))

        def _parse_four_star_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        four_star_count = _parse_four_star_count(d.pop("fourStarCount", UNSET))

        def _parse_five_star_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        five_star_count = _parse_five_star_count(d.pop("fiveStarCount", UNSET))

        hotel_property_response_200_output_property_ratings_breakdown_type_0 = cls(
            one_star_count=one_star_count,
            two_star_count=two_star_count,
            three_star_count=three_star_count,
            four_star_count=four_star_count,
            five_star_count=five_star_count,
        )

        hotel_property_response_200_output_property_ratings_breakdown_type_0.additional_properties = d
        return hotel_property_response_200_output_property_ratings_breakdown_type_0

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
