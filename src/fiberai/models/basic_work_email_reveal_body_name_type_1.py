from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.basic_work_email_reveal_body_name_type_1_mode import BasicWorkEmailRevealBodyNameType1Mode

T = TypeVar("T", bound="BasicWorkEmailRevealBodyNameType1")


@_attrs_define
class BasicWorkEmailRevealBodyNameType1:
    """
    Attributes:
        mode (BasicWorkEmailRevealBodyNameType1Mode):
        first_name (str): First name of the person.
        last_name (str): Last name of the person.
    """

    mode: BasicWorkEmailRevealBodyNameType1Mode
    first_name: str
    last_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = BasicWorkEmailRevealBodyNameType1Mode(d.pop("mode"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        basic_work_email_reveal_body_name_type_1 = cls(
            mode=mode,
            first_name=first_name,
            last_name=last_name,
        )

        basic_work_email_reveal_body_name_type_1.additional_properties = d
        return basic_work_email_reveal_body_name_type_1

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
