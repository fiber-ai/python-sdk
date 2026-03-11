from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemAcquisitionsType0Item")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemAcquisitionsType0Item:
    """
    Attributes:
        price_usd (float | None | Unset):
        acquiree_name (None | str | Unset):
        acquisition_date (None | str | Unset):
    """

    price_usd: float | None | Unset = UNSET
    acquiree_name: None | str | Unset = UNSET
    acquisition_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price_usd: float | None | Unset
        if isinstance(self.price_usd, Unset):
            price_usd = UNSET
        else:
            price_usd = self.price_usd

        acquiree_name: None | str | Unset
        if isinstance(self.acquiree_name, Unset):
            acquiree_name = UNSET
        else:
            acquiree_name = self.acquiree_name

        acquisition_date: None | str | Unset
        if isinstance(self.acquisition_date, Unset):
            acquisition_date = UNSET
        else:
            acquisition_date = self.acquisition_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if acquiree_name is not UNSET:
            field_dict["acquiree_name"] = acquiree_name
        if acquisition_date is not UNSET:
            field_dict["acquisition_date"] = acquisition_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_price_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_usd = _parse_price_usd(d.pop("price_usd", UNSET))

        def _parse_acquiree_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquiree_name = _parse_acquiree_name(d.pop("acquiree_name", UNSET))

        def _parse_acquisition_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquisition_date = _parse_acquisition_date(d.pop("acquisition_date", UNSET))

        kitchen_sink_company_response_200_output_data_item_acquisitions_type_0_item = cls(
            price_usd=price_usd,
            acquiree_name=acquiree_name,
            acquisition_date=acquisition_date,
        )

        kitchen_sink_company_response_200_output_data_item_acquisitions_type_0_item.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_acquisitions_type_0_item

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
