from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quick_person_resolve_response_200_output_data_item_identifier import (
    QuickPersonResolveResponse200OutputDataItemIdentifier,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_person_resolve_response_200_output_data_item_person_type_0 import (
        QuickPersonResolveResponse200OutputDataItemPersonType0,
    )


T = TypeVar("T", bound="QuickPersonResolveResponse200OutputDataItem")


@_attrs_define
class QuickPersonResolveResponse200OutputDataItem:
    """
    Attributes:
        identifier (QuickPersonResolveResponse200OutputDataItemIdentifier): The identifier type you supplied, echoed
            back.
        value (str): The identifier value you supplied, echoed back.
        found (bool):
        person (None | QuickPersonResolveResponse200OutputDataItemPersonType0 | Unset):
    """

    identifier: QuickPersonResolveResponse200OutputDataItemIdentifier
    value: str
    found: bool
    person: None | QuickPersonResolveResponse200OutputDataItemPersonType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_person_resolve_response_200_output_data_item_person_type_0 import (
            QuickPersonResolveResponse200OutputDataItemPersonType0,  # noqa: PLC0415
        )

        identifier = self.identifier.value

        value = self.value

        found = self.found

        person: dict[str, Any] | None | Unset
        if isinstance(self.person, Unset):
            person = UNSET
        elif isinstance(self.person, QuickPersonResolveResponse200OutputDataItemPersonType0):
            person = self.person.to_dict()
        else:
            person = self.person

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "value": value,
                "found": found,
            }
        )
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_person_resolve_response_200_output_data_item_person_type_0 import (
            QuickPersonResolveResponse200OutputDataItemPersonType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        identifier = QuickPersonResolveResponse200OutputDataItemIdentifier(d.pop("identifier"))

        value = d.pop("value")

        found = d.pop("found")

        def _parse_person(data: object) -> None | QuickPersonResolveResponse200OutputDataItemPersonType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_type_0 = QuickPersonResolveResponse200OutputDataItemPersonType0.from_dict(data)

                return person_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuickPersonResolveResponse200OutputDataItemPersonType0 | Unset, data)

        person = _parse_person(d.pop("person", UNSET))

        quick_person_resolve_response_200_output_data_item = cls(
            identifier=identifier,
            value=value,
            found=found,
            person=person,
        )

        quick_person_resolve_response_200_output_data_item.additional_properties = d
        return quick_person_resolve_response_200_output_data_item

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
