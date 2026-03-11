from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_profile_search_params_response_402_out_of_credits_alert_type_0 import (
        TextToProfileSearchParamsResponse402OutOfCreditsAlertType0,
    )


T = TypeVar("T", bound="TextToProfileSearchParamsResponse402")


@_attrs_define
class TextToProfileSearchParamsResponse402:
    """
    Attributes:
        message (str): The error message.
        out_of_credits_alert (None | TextToProfileSearchParamsResponse402OutOfCreditsAlertType0 | Unset): Present on 402
            responses. Contains a link to get more credits.
    """

    message: str
    out_of_credits_alert: None | TextToProfileSearchParamsResponse402OutOfCreditsAlertType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_profile_search_params_response_402_out_of_credits_alert_type_0 import (
            TextToProfileSearchParamsResponse402OutOfCreditsAlertType0,
        )

        message = self.message

        out_of_credits_alert: dict[str, Any] | None | Unset
        if isinstance(self.out_of_credits_alert, Unset):
            out_of_credits_alert = UNSET
        elif isinstance(self.out_of_credits_alert, TextToProfileSearchParamsResponse402OutOfCreditsAlertType0):
            out_of_credits_alert = self.out_of_credits_alert.to_dict()
        else:
            out_of_credits_alert = self.out_of_credits_alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if out_of_credits_alert is not UNSET:
            field_dict["outOfCreditsAlert"] = out_of_credits_alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_params_response_402_out_of_credits_alert_type_0 import (
            TextToProfileSearchParamsResponse402OutOfCreditsAlertType0,
        )

        d = dict(src_dict)
        message = d.pop("message")

        def _parse_out_of_credits_alert(
            data: object,
        ) -> None | TextToProfileSearchParamsResponse402OutOfCreditsAlertType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                out_of_credits_alert_type_0 = TextToProfileSearchParamsResponse402OutOfCreditsAlertType0.from_dict(data)

                return out_of_credits_alert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToProfileSearchParamsResponse402OutOfCreditsAlertType0 | Unset, data)

        out_of_credits_alert = _parse_out_of_credits_alert(d.pop("outOfCreditsAlert", UNSET))

        text_to_profile_search_params_response_402 = cls(
            message=message,
            out_of_credits_alert=out_of_credits_alert,
        )

        text_to_profile_search_params_response_402.additional_properties = d
        return text_to_profile_search_params_response_402

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
