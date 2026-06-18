from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScalarDeltaChange")


@_attrs_define
class ScalarDeltaChange:
    """
    Attributes:
        kind (Literal['scalar']):
        previous (bool | None | str): Previous value
        current (bool | None | str): Current value
    """

    kind: Literal["scalar"]
    previous: bool | None | str
    current: bool | None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        previous: bool | None | str
        previous = self.previous

        current: bool | None | str
        current = self.current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "previous": previous,
                "current": current,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["scalar"], d.pop("kind"))
        if kind != "scalar":
            raise ValueError(f"kind must match const 'scalar', got '{kind}'")

        def _parse_previous(data: object) -> bool | None | str:
            if data is None:
                return data
            return cast(bool | None | str, data)

        previous = _parse_previous(d.pop("previous"))

        def _parse_current(data: object) -> bool | None | str:
            if data is None:
                return data
            return cast(bool | None | str, data)

        current = _parse_current(d.pop("current"))

        scalar_delta_change = cls(
            kind=kind,
            previous=previous,
            current=current,
        )

        scalar_delta_change.additional_properties = d
        return scalar_delta_change

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
