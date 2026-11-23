from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_tracker_entity_limit_body_entity_type import UpdateTrackerEntityLimitBodyEntityType
from ..models.update_tracker_entity_limit_body_operation import UpdateTrackerEntityLimitBodyOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTrackerEntityLimitBody")


@_attrs_define
class UpdateTrackerEntityLimitBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        entity_type (UpdateTrackerEntityLimitBodyEntityType): Which limit to change: the one on tracked companies or the
            one on tracked people.
        operation (UpdateTrackerEntityLimitBodyOperation): set: pin an absolute limit. increase/decrease: adjust the
            current limit by count. remove: remove the limit. increase and decrease have no effect when there is no limit;
            use set to establish one first.
        count (int | None | Unset): Number of companies or people. Required for set (zero or greater), increase and
            decrease (greater than zero); omit it for remove.
    """

    api_key: str
    entity_type: UpdateTrackerEntityLimitBodyEntityType
    operation: UpdateTrackerEntityLimitBodyOperation
    count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        entity_type = self.entity_type.value

        operation = self.operation.value

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "entityType": entity_type,
                "operation": operation,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        entity_type = UpdateTrackerEntityLimitBodyEntityType(d.pop("entityType"))

        operation = UpdateTrackerEntityLimitBodyOperation(d.pop("operation"))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        update_tracker_entity_limit_body = cls(
            api_key=api_key,
            entity_type=entity_type,
            operation=operation,
            count=count,
        )

        update_tracker_entity_limit_body.additional_properties = d
        return update_tracker_entity_limit_body

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
