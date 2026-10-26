from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_talent_flow_body_render_image_type_0_format import GetTalentFlowBodyRenderImageType0Format
from ..models.get_talent_flow_body_render_image_type_0_theme_type_1 import GetTalentFlowBodyRenderImageType0ThemeType1
from ..models.get_talent_flow_body_render_image_type_0_theme_type_2_type_1 import (
    GetTalentFlowBodyRenderImageType0ThemeType2Type1,
)
from ..models.get_talent_flow_body_render_image_type_0_theme_type_3_type_1 import (
    GetTalentFlowBodyRenderImageType0ThemeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTalentFlowBodyRenderImageType0")


@_attrs_define
class GetTalentFlowBodyRenderImageType0:
    """
    Attributes:
        enabled (bool): Set true to also generate a shareable talent-flow graphic image covering both joiners and
            leavers. The image URL is returned in the response's graphic field.
        format_ (GetTalentFlowBodyRenderImageType0Format): File format of the generated graphic.
        theme (GetTalentFlowBodyRenderImageType0ThemeType1 | GetTalentFlowBodyRenderImageType0ThemeType2Type1 |
            GetTalentFlowBodyRenderImageType0ThemeType3Type1 | None | Unset): Color palette for the graphic. Omit to use the
            default palette.
        accent_color (None | str | Unset): Optional brand color as a 6-digit hex string (e.g. '#7C5CFF'). Applied to the
            center card and the joiners side; the leavers side keeps the theme's complementary color. Omit to use the
            theme's built-in color.
    """

    enabled: bool
    format_: GetTalentFlowBodyRenderImageType0Format
    theme: (
        GetTalentFlowBodyRenderImageType0ThemeType1
        | GetTalentFlowBodyRenderImageType0ThemeType2Type1
        | GetTalentFlowBodyRenderImageType0ThemeType3Type1
        | None
        | Unset
    ) = UNSET
    accent_color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        format_ = self.format_.value

        theme: None | str | Unset
        if isinstance(self.theme, Unset):
            theme = UNSET
        elif isinstance(self.theme, GetTalentFlowBodyRenderImageType0ThemeType1):
            theme = self.theme.value
        elif isinstance(self.theme, GetTalentFlowBodyRenderImageType0ThemeType2Type1):
            theme = self.theme.value
        elif isinstance(self.theme, GetTalentFlowBodyRenderImageType0ThemeType3Type1):
            theme = self.theme.value
        else:
            theme = self.theme

        accent_color: None | str | Unset
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "format": format_,
            }
        )
        if theme is not UNSET:
            field_dict["theme"] = theme
        if accent_color is not UNSET:
            field_dict["accentColor"] = accent_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        format_ = GetTalentFlowBodyRenderImageType0Format(d.pop("format"))

        def _parse_theme(
            data: object,
        ) -> (
            GetTalentFlowBodyRenderImageType0ThemeType1
            | GetTalentFlowBodyRenderImageType0ThemeType2Type1
            | GetTalentFlowBodyRenderImageType0ThemeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_1 = GetTalentFlowBodyRenderImageType0ThemeType1(data)

                return theme_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_2_type_1 = GetTalentFlowBodyRenderImageType0ThemeType2Type1(data)

                return theme_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_3_type_1 = GetTalentFlowBodyRenderImageType0ThemeType3Type1(data)

                return theme_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetTalentFlowBodyRenderImageType0ThemeType1
                | GetTalentFlowBodyRenderImageType0ThemeType2Type1
                | GetTalentFlowBodyRenderImageType0ThemeType3Type1
                | None
                | Unset,
                data,
            )

        theme = _parse_theme(d.pop("theme", UNSET))

        def _parse_accent_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accent_color = _parse_accent_color(d.pop("accentColor", UNSET))

        get_talent_flow_body_render_image_type_0 = cls(
            enabled=enabled,
            format_=format_,
            theme=theme,
            accent_color=accent_color,
        )

        get_talent_flow_body_render_image_type_0.additional_properties = d
        return get_talent_flow_body_render_image_type_0

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
