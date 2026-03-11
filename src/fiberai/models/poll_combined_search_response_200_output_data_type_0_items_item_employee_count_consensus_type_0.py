from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemEmployeeCountConsensusType0")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemEmployeeCountConsensusType0:
    """
    Attributes:
        gte (float | None | Unset):
        lte (float | None | Unset):
    """

    gte: float | None | Unset = UNSET
    lte: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gte: float | None | Unset
        if isinstance(self.gte, Unset):
            gte = UNSET
        else:
            gte = self.gte

        lte: float | None | Unset
        if isinstance(self.lte, Unset):
            lte = UNSET
        else:
            lte = self.lte

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gte is not UNSET:
            field_dict["gte"] = gte
        if lte is not UNSET:
            field_dict["lte"] = lte

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_gte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gte = _parse_gte(d.pop("gte", UNSET))

        def _parse_lte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lte = _parse_lte(d.pop("lte", UNSET))

        poll_combined_search_response_200_output_data_type_0_items_item_employee_count_consensus_type_0 = cls(
            gte=gte,
            lte=lte,
        )

        poll_combined_search_response_200_output_data_type_0_items_item_employee_count_consensus_type_0.additional_properties = d
        return poll_combined_search_response_200_output_data_type_0_items_item_employee_count_consensus_type_0

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
