from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup_levels_item import (
        GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookupLevelsItem,
    )


T = TypeVar("T", bound="GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup")


@_attrs_define
class GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup:
    """
    Attributes:
        levels (list[GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookupLevelsItem]):
    """

    levels: list[GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookupLevelsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.to_dict()
            levels.append(levels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "levels": levels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup_levels_item import (
            GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookupLevelsItem,
        )

        d = dict(src_dict)
        levels = []
        _levels = d.pop("levels")
        for levels_item_data in _levels:
            levels_item = (
                GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookupLevelsItem.from_dict(
                    levels_item_data
                )
            )

            levels.append(levels_item)

        get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup = cls(
            levels=levels,
        )

        get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup.additional_properties = d
        return get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup

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
