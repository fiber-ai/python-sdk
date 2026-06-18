from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddTrackerCompaniesResponse200OutputInvalidCompaniesItem")


@_attrs_define
class AddTrackerCompaniesResponse200OutputInvalidCompaniesItem:
    """
    Attributes:
        index (int): Index in the input array.
        reason (str): Why this company was skipped.
    """

    index: int
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        reason = d.pop("reason")

        add_tracker_companies_response_200_output_invalid_companies_item = cls(
            index=index,
            reason=reason,
        )

        add_tracker_companies_response_200_output_invalid_companies_item.additional_properties = d
        return add_tracker_companies_response_200_output_invalid_companies_item

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
