from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_status_changed_to_statuses_type_0_item import CompanyStatusChangedToStatusesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyStatusChanged")


@_attrs_define
class CompanyStatusChanged:
    """
    Attributes:
        type_ (Literal['company_status_changed']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        to_statuses (list[CompanyStatusChangedToStatusesType0Item] | None | Unset): Only alert if new status is one of
            these. Omit for any status change.
    """

    type_: Literal["company_status_changed"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    to_statuses: list[CompanyStatusChangedToStatusesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        to_statuses: list[str] | None | Unset
        if isinstance(self.to_statuses, Unset):
            to_statuses = UNSET
        elif isinstance(self.to_statuses, list):
            to_statuses = []
            for to_statuses_type_0_item_data in self.to_statuses:
                to_statuses_type_0_item = to_statuses_type_0_item_data.value
                to_statuses.append(to_statuses_type_0_item)

        else:
            to_statuses = self.to_statuses

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
        if to_statuses is not UNSET:
            field_dict["toStatuses"] = to_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["company_status_changed"], d.pop("type"))
        if type_ != "company_status_changed":
            raise ValueError(f"type must match const 'company_status_changed', got '{type_}'")

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

        def _parse_to_statuses(data: object) -> list[CompanyStatusChangedToStatusesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_statuses_type_0 = []
                _to_statuses_type_0 = data
                for to_statuses_type_0_item_data in _to_statuses_type_0:
                    to_statuses_type_0_item = CompanyStatusChangedToStatusesType0Item(to_statuses_type_0_item_data)

                    to_statuses_type_0.append(to_statuses_type_0_item)

                return to_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyStatusChangedToStatusesType0Item] | None | Unset, data)

        to_statuses = _parse_to_statuses(d.pop("toStatuses", UNSET))

        company_status_changed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            to_statuses=to_statuses,
        )

        company_status_changed.additional_properties = d
        return company_status_changed

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
