from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTalentFlowResponse200OutputWindow")


@_attrs_define
class GetTalentFlowResponse200OutputWindow:
    """Time window for the analysis.

    Attributes:
        after (None | str | Unset): Start of the analysis window (YYYY-MM-DD). Null means no lower bound.
        before (None | str | Unset): End of the analysis window (YYYY-MM-DD). Null means no upper bound.
    """

    after: None | str | Unset = UNSET
    before: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after: None | str | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        before: None | str | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        else:
            before = self.before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after = _parse_after(d.pop("after", UNSET))

        def _parse_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        before = _parse_before(d.pop("before", UNSET))

        get_talent_flow_response_200_output_window = cls(
            after=after,
            before=before,
        )

        get_talent_flow_response_200_output_window.additional_properties = d
        return get_talent_flow_response_200_output_window

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
