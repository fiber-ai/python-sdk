from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lite_contact_reveal_body_input_type_0_mode import LiteContactRevealBodyInputType0Mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiteContactRevealBodyInputType0")


@_attrs_define
class LiteContactRevealBodyInputType0:
    """
    Attributes:
        mode (LiteContactRevealBodyInputType0Mode):
        linkedin_identifier (str): LinkedIn profile identifier — a full URL, bare slug, or URN (e.g. 'williamhgates',
            'https://www.linkedin.com/in/williamhgates').
        full_name (None | str | Unset): Full name of the person. Optional — improves match accuracy.
    """

    mode: LiteContactRevealBodyInputType0Mode
    linkedin_identifier: str
    full_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        linkedin_identifier = self.linkedin_identifier

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "linkedinIdentifier": linkedin_identifier,
            }
        )
        if full_name is not UNSET:
            field_dict["fullName"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = LiteContactRevealBodyInputType0Mode(d.pop("mode"))

        linkedin_identifier = d.pop("linkedinIdentifier")

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))

        lite_contact_reveal_body_input_type_0 = cls(
            mode=mode,
            linkedin_identifier=linkedin_identifier,
            full_name=full_name,
        )

        lite_contact_reveal_body_input_type_0.additional_properties = d
        return lite_contact_reveal_body_input_type_0

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
