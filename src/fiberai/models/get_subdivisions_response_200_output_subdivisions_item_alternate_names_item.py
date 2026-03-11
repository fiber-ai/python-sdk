from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem")


@_attrs_define
class GetSubdivisionsResponse200OutputSubdivisionsItemAlternateNamesItem:
    """
    Attributes:
        name (str): The alternate name
        language_code (str): ISO 639 language code (e.g. 'eng', 'hin', 'deu'). See
            https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes to map codes to full language names.
    """

    name: str
    language_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "languageCode": language_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        language_code = d.pop("languageCode")

        get_subdivisions_response_200_output_subdivisions_item_alternate_names_item = cls(
            name=name,
            language_code=language_code,
        )

        get_subdivisions_response_200_output_subdivisions_item_alternate_names_item.additional_properties = d
        return get_subdivisions_response_200_output_subdivisions_item_alternate_names_item

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
