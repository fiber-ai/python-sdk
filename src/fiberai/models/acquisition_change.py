from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AcquisitionChange")


@_attrs_define
class AcquisitionChange:
    """
    Attributes:
        acquiree_name (str): Name of the acquired company
        acquiree_uuid (None | str): Unique identifier
        acquiree_url (None | str): Reference URL
        price_usd (float | None): Acquisition price in USD
        acquisition_date (None | str): ISO date of acquisition
    """

    acquiree_name: str
    acquiree_uuid: None | str
    acquiree_url: None | str
    price_usd: float | None
    acquisition_date: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acquiree_name = self.acquiree_name

        acquiree_uuid: None | str
        acquiree_uuid = self.acquiree_uuid

        acquiree_url: None | str
        acquiree_url = self.acquiree_url

        price_usd: float | None
        price_usd = self.price_usd

        acquisition_date: None | str
        acquisition_date = self.acquisition_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acquireeName": acquiree_name,
                "acquireeUuid": acquiree_uuid,
                "acquireeUrl": acquiree_url,
                "priceUsd": price_usd,
                "acquisitionDate": acquisition_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acquiree_name = d.pop("acquireeName")

        def _parse_acquiree_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acquiree_uuid = _parse_acquiree_uuid(d.pop("acquireeUuid"))

        def _parse_acquiree_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acquiree_url = _parse_acquiree_url(d.pop("acquireeUrl"))

        def _parse_price_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price_usd = _parse_price_usd(d.pop("priceUsd"))

        def _parse_acquisition_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acquisition_date = _parse_acquisition_date(d.pop("acquisitionDate"))

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
