from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyCreditsResponse402")


@_attrs_define
class BuyCreditsResponse402:
    """
    Attributes:
        message (str): The error message.
        decline_code (None | str | Unset): Why the payment was declined, when the reason is known — for example
            'insufficient_funds' or 'expired_card'.
    """

    message: str
    decline_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        decline_code: None | str | Unset
        if isinstance(self.decline_code, Unset):
            decline_code = UNSET
        else:
            decline_code = self.decline_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if decline_code is not UNSET:
            field_dict["declineCode"] = decline_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        def _parse_decline_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decline_code = _parse_decline_code(d.pop("declineCode", UNSET))

        buy_credits_response_402 = cls(
            message=message,
            decline_code=decline_code,
        )

        buy_credits_response_402.additional_properties = d
        return buy_credits_response_402

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
