from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_talent_flow_response_200_output_graphic_type_0_format import (
    GetTalentFlowResponse200OutputGraphicType0Format,
)

T = TypeVar("T", bound="GetTalentFlowResponse200OutputGraphicType0")


@_attrs_define
class GetTalentFlowResponse200OutputGraphicType0:
    """Shareable talent-flow graphic image covering both joiners and leavers. Present when renderImage.enabled was set and
    a graphic could be generated; null otherwise (for example when no talent movement was found in the window).

        Attributes:
            url (str): URL of the hosted talent-flow graphic image.
            format_ (GetTalentFlowResponse200OutputGraphicType0Format): File format of the graphic image.
    """

    url: str
    format_: GetTalentFlowResponse200OutputGraphicType0Format
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        format_ = self.format_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        format_ = GetTalentFlowResponse200OutputGraphicType0Format(d.pop("format"))

        get_talent_flow_response_200_output_graphic_type_0 = cls(
            url=url,
            format_=format_,
        )

        get_talent_flow_response_200_output_graphic_type_0.additional_properties = d
        return get_talent_flow_response_200_output_graphic_type_0

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
