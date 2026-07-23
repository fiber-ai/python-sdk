from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RefreshTrackerCompanyListResponse200Output")


@_attrs_define
class RefreshTrackerCompanyListResponse200Output:
    """
    Attributes:
        entity_count (int): Number of entities that will be processed.
        estimated_credits (float): Estimated credit cost for this refresh. Actual cost may vary based on organization
            pricing or if tracked entities change before processing completes.
        message (str): Human-readable confirmation of the refresh initiation.
    """

    entity_count: int
    estimated_credits: float
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_count = self.entity_count

        estimated_credits = self.estimated_credits

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityCount": entity_count,
                "estimatedCredits": estimated_credits,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_count = d.pop("entityCount")

        estimated_credits = d.pop("estimatedCredits")

        message = d.pop("message")

        refresh_tracker_company_list_response_200_output = cls(
            entity_count=entity_count,
            estimated_credits=estimated_credits,
            message=message,
        )

        refresh_tracker_company_list_response_200_output.additional_properties = d
        return refresh_tracker_company_list_response_200_output

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
