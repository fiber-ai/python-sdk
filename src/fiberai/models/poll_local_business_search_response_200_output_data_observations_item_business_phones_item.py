from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem:
    """
    Attributes:
        phone_number (str):
        country_code (None | str | Unset):
        country_calling_code (float | None | Unset):
    """

    phone_number: str
    country_code: None | str | Unset = UNSET
    country_calling_code: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        country_calling_code: float | None | Unset
        if isinstance(self.country_calling_code, Unset):
            country_calling_code = UNSET
        else:
            country_calling_code = self.country_calling_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phoneNumber": phone_number,
            }
        )
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if country_calling_code is not UNSET:
            field_dict["countryCallingCode"] = country_calling_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_number = d.pop("phoneNumber")

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_country_calling_code(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        country_calling_code = _parse_country_calling_code(d.pop("countryCallingCode", UNSET))

        poll_local_business_search_response_200_output_data_observations_item_business_phones_item = cls(
            phone_number=phone_number,
            country_code=country_code,
            country_calling_code=country_calling_code,
        )

        poll_local_business_search_response_200_output_data_observations_item_business_phones_item.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_business_phones_item

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
