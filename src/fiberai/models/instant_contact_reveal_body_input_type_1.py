from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instant_contact_reveal_body_input_type_1_mode import InstantContactRevealBodyInputType1Mode

T = TypeVar("T", bound="InstantContactRevealBodyInputType1")


@_attrs_define
class InstantContactRevealBodyInputType1:
    """
    Attributes:
        mode (InstantContactRevealBodyInputType1Mode):
        full_name (str): Full name of the person.
        company_domain (str): Company domain (e.g. 'gatesfoundation.org').
    """

    mode: InstantContactRevealBodyInputType1Mode
    full_name: str
    company_domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        full_name = self.full_name

        company_domain = self.company_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "fullName": full_name,
                "companyDomain": company_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = InstantContactRevealBodyInputType1Mode(d.pop("mode"))

        full_name = d.pop("fullName")

        company_domain = d.pop("companyDomain")

        instant_contact_reveal_body_input_type_1 = cls(
            mode=mode,
            full_name=full_name,
            company_domain=company_domain,
        )

        instant_contact_reveal_body_input_type_1.additional_properties = d
        return instant_contact_reveal_body_input_type_1

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
