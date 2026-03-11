from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_profile_search_response_200_output_data_item_tenures_type_0_item_date_range import (
        TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange,
    )


T = TypeVar("T", bound="TextToProfileSearchResponse200OutputDataItemTenuresType0Item")


@_attrs_define
class TextToProfileSearchResponse200OutputDataItemTenuresType0Item:
    """
    Attributes:
        date_range (TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange):
        titles (list[str]):
        localities (list[str]):
        linkedin_company_id (None | str | Unset):
        company_name (None | str | Unset):
        range_length_days (float | None | Unset):
    """

    date_range: TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange
    titles: list[str]
    localities: list[str]
    linkedin_company_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    range_length_days: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_range = self.date_range.to_dict()

        titles = self.titles

        localities = self.localities

        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        range_length_days: float | None | Unset
        if isinstance(self.range_length_days, Unset):
            range_length_days = UNSET
        else:
            range_length_days = self.range_length_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_range": date_range,
                "titles": titles,
                "localities": localities,
            }
        )
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if range_length_days is not UNSET:
            field_dict["range_length_days"] = range_length_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_response_200_output_data_item_tenures_type_0_item_date_range import (
            TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange,
        )

        d = dict(src_dict)
        date_range = TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange.from_dict(
            d.pop("date_range")
        )

        titles = cast(list[str], d.pop("titles"))

        localities = cast(list[str], d.pop("localities"))

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_range_length_days(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_length_days = _parse_range_length_days(d.pop("range_length_days", UNSET))

        text_to_profile_search_response_200_output_data_item_tenures_type_0_item = cls(
            date_range=date_range,
            titles=titles,
            localities=localities,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            range_length_days=range_length_days,
        )

        text_to_profile_search_response_200_output_data_item_tenures_type_0_item.additional_properties = d
        return text_to_profile_search_response_200_output_data_item_tenures_type_0_item

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
