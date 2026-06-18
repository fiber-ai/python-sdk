from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.funding_stage_changed_to_stages_type_0_item import FundingStageChangedToStagesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="FundingStageChanged")


@_attrs_define
class FundingStageChanged:
    """
    Attributes:
        type_ (Literal['funding_stage_changed']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        to_stages (list[FundingStageChangedToStagesType0Item] | None | Unset): Only alert if new stage is one of these.
            Omit for any stage change.
    """

    type_: Literal["funding_stage_changed"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    to_stages: list[FundingStageChangedToStagesType0Item] | None | Unset = UNSET
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

        to_stages: list[str] | None | Unset
        if isinstance(self.to_stages, Unset):
            to_stages = UNSET
        elif isinstance(self.to_stages, list):
            to_stages = []
            for to_stages_type_0_item_data in self.to_stages:
                to_stages_type_0_item = to_stages_type_0_item_data.value
                to_stages.append(to_stages_type_0_item)

        else:
            to_stages = self.to_stages

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
        if to_stages is not UNSET:
            field_dict["toStages"] = to_stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["funding_stage_changed"], d.pop("type"))
        if type_ != "funding_stage_changed":
            raise ValueError(f"type must match const 'funding_stage_changed', got '{type_}'")

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

        def _parse_to_stages(data: object) -> list[FundingStageChangedToStagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_stages_type_0 = []
                _to_stages_type_0 = data
                for to_stages_type_0_item_data in _to_stages_type_0:
                    to_stages_type_0_item = FundingStageChangedToStagesType0Item(to_stages_type_0_item_data)

                    to_stages_type_0.append(to_stages_type_0_item)

                return to_stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FundingStageChangedToStagesType0Item] | None | Unset, data)

        to_stages = _parse_to_stages(d.pop("toStages", UNSET))

        funding_stage_changed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            to_stages=to_stages,
        )

        funding_stage_changed.additional_properties = d
        return funding_stage_changed

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
