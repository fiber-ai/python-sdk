from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcquisitionChange")


@_attrs_define
class AcquisitionChange:
    """
    Attributes:
        acquiree_name (str): Name of the acquired company
        acquiree_uuid (None | str | Unset): Unique identifier
        acquiree_url (None | str | Unset): Reference URL
        price_usd (float | None | Unset): Acquisition price in USD
        acquisition_date (None | str | Unset): ISO date of acquisition
    """

    acquiree_name: str
    acquiree_uuid: None | str | Unset = UNSET
    acquiree_url: None | str | Unset = UNSET
    price_usd: float | None | Unset = UNSET
    acquisition_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acquiree_name = self.acquiree_name

        acquiree_uuid: None | str | Unset
        if isinstance(self.acquiree_uuid, Unset):
            acquiree_uuid = UNSET
        else:
            acquiree_uuid = self.acquiree_uuid

        acquiree_url: None | str | Unset
        if isinstance(self.acquiree_url, Unset):
            acquiree_url = UNSET
        else:
            acquiree_url = self.acquiree_url

        price_usd: float | None | Unset
        if isinstance(self.price_usd, Unset):
            price_usd = UNSET
        else:
            price_usd = self.price_usd

        acquisition_date: None | str | Unset
        if isinstance(self.acquisition_date, Unset):
            acquisition_date = UNSET
        else:
            acquisition_date = self.acquisition_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acquireeName": acquiree_name,
            }
        )
        if acquiree_uuid is not UNSET:
            field_dict["acquireeUuid"] = acquiree_uuid
        if acquiree_url is not UNSET:
            field_dict["acquireeUrl"] = acquiree_url
        if price_usd is not UNSET:
            field_dict["priceUsd"] = price_usd
        if acquisition_date is not UNSET:
            field_dict["acquisitionDate"] = acquisition_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acquiree_name = d.pop("acquireeName")

        def _parse_acquiree_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquiree_uuid = _parse_acquiree_uuid(d.pop("acquireeUuid", UNSET))

        def _parse_acquiree_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquiree_url = _parse_acquiree_url(d.pop("acquireeUrl", UNSET))

        def _parse_price_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_usd = _parse_price_usd(d.pop("priceUsd", UNSET))

        def _parse_acquisition_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquisition_date = _parse_acquisition_date(d.pop("acquisitionDate", UNSET))

        acquisition_change = cls(
            acquiree_name=acquiree_name,
            acquiree_uuid=acquiree_uuid,
            acquiree_url=acquiree_url,
            price_usd=price_usd,
            acquisition_date=acquisition_date,
        )

        acquisition_change.additional_properties = d
        return acquisition_change

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
