from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.joined_an_accelerator_accelerator_names_type_0_item import JoinedAnAcceleratorAcceleratorNamesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinedAnAccelerator")


@_attrs_define
class JoinedAnAccelerator:
    """
    Attributes:
        type_ (Literal['joined_accelerator']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        accelerator_names (list[JoinedAnAcceleratorAcceleratorNamesType0Item] | None | Unset): Only alert when the
            company joins one of these accelerators. Omit for any accelerator. There is no batch selection: companies always
            join the latest batch.
    """

    type_: Literal["joined_accelerator"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    accelerator_names: list[JoinedAnAcceleratorAcceleratorNamesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        accelerator_names: list[str] | None | Unset
        if isinstance(self.accelerator_names, Unset):
            accelerator_names = UNSET
        elif isinstance(self.accelerator_names, list):
            accelerator_names = []
            for accelerator_names_type_0_item_data in self.accelerator_names:
                accelerator_names_type_0_item = accelerator_names_type_0_item_data.value
                accelerator_names.append(accelerator_names_type_0_item)

        else:
            accelerator_names = self.accelerator_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if accelerator_names is not UNSET:
            field_dict["acceleratorNames"] = accelerator_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["joined_accelerator"], d.pop("type"))
        if type_ != "joined_accelerator":
            raise ValueError(f"type must match const 'joined_accelerator', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_accelerator_names(data: object) -> list[JoinedAnAcceleratorAcceleratorNamesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accelerator_names_type_0 = []
                _accelerator_names_type_0 = data
                for accelerator_names_type_0_item_data in _accelerator_names_type_0:
                    accelerator_names_type_0_item = JoinedAnAcceleratorAcceleratorNamesType0Item(
                        accelerator_names_type_0_item_data
                    )

                    accelerator_names_type_0.append(accelerator_names_type_0_item)

                return accelerator_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JoinedAnAcceleratorAcceleratorNamesType0Item] | None | Unset, data)

        accelerator_names = _parse_accelerator_names(d.pop("acceleratorNames", UNSET))

        joined_an_accelerator = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            accelerator_names=accelerator_names,
        )

        joined_an_accelerator.additional_properties = d
        return joined_an_accelerator

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
