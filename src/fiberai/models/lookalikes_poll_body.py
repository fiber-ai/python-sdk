from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookalikesPollBody")


@_attrs_define
class LookalikesPollBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        lookalike_run_id (str): Identifier of a lookalike run, returned when the run started.
    """

    api_key: str
    lookalike_run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        lookalike_run_id = self.lookalike_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "lookalikeRunId": lookalike_run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        lookalike_run_id = d.pop("lookalikeRunId")

        lookalikes_poll_body = cls(
            api_key=api_key,
            lookalike_run_id=lookalike_run_id,
        )

        lookalikes_poll_body.additional_properties = d
        return lookalikes_poll_body

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
