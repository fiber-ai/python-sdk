from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_auto_topup_settings_response_200_output_settings_item_type_0 import (
        GetAutoTopupSettingsResponse200OutputSettingsItemType0,
    )
    from ..models.get_auto_topup_settings_response_200_output_settings_item_type_1 import (
        GetAutoTopupSettingsResponse200OutputSettingsItemType1,
    )


T = TypeVar("T", bound="GetAutoTopupSettingsResponse200Output")


@_attrs_define
class GetAutoTopupSettingsResponse200Output:
    """
    Attributes:
        settings (list[GetAutoTopupSettingsResponse200OutputSettingsItemType0 |
            GetAutoTopupSettingsResponse200OutputSettingsItemType1]): Auto top-up settings per subscription
    """

    settings: list[
        GetAutoTopupSettingsResponse200OutputSettingsItemType0 | GetAutoTopupSettingsResponse200OutputSettingsItemType1
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_auto_topup_settings_response_200_output_settings_item_type_0 import (
            GetAutoTopupSettingsResponse200OutputSettingsItemType0,
        )

        settings = []
        for settings_item_data in self.settings:
            settings_item: dict[str, Any]
            if isinstance(settings_item_data, GetAutoTopupSettingsResponse200OutputSettingsItemType0):
                settings_item = settings_item_data.to_dict()
            else:
                settings_item = settings_item_data.to_dict()

            settings.append(settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_auto_topup_settings_response_200_output_settings_item_type_0 import (
            GetAutoTopupSettingsResponse200OutputSettingsItemType0,
        )
        from ..models.get_auto_topup_settings_response_200_output_settings_item_type_1 import (
            GetAutoTopupSettingsResponse200OutputSettingsItemType1,
        )

        d = dict(src_dict)
        settings = []
        _settings = d.pop("settings")
        for settings_item_data in _settings:

            def _parse_settings_item(
                data: object,
            ) -> (
                GetAutoTopupSettingsResponse200OutputSettingsItemType0
                | GetAutoTopupSettingsResponse200OutputSettingsItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    settings_item_type_0 = GetAutoTopupSettingsResponse200OutputSettingsItemType0.from_dict(data)

                    return settings_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                settings_item_type_1 = GetAutoTopupSettingsResponse200OutputSettingsItemType1.from_dict(data)

                return settings_item_type_1

            settings_item = _parse_settings_item(settings_item_data)

            settings.append(settings_item)

        get_auto_topup_settings_response_200_output = cls(
            settings=settings,
        )

        get_auto_topup_settings_response_200_output.additional_properties = d
        return get_auto_topup_settings_response_200_output

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
