from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cards_attach_response_500_type_0_reason import CardsAttachResponse500Type0Reason
from ..models.cards_attach_response_500_type_0_status import CardsAttachResponse500Type0Status

T = TypeVar("T", bound="CardsAttachResponse500Type0")


@_attrs_define
class CardsAttachResponse500Type0:
    """
    Attributes:
        status (CardsAttachResponse500Type0Status):
        reason (CardsAttachResponse500Type0Reason):
        message (str):
    """

    status: CardsAttachResponse500Type0Status
    reason: CardsAttachResponse500Type0Reason
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        reason = self.reason.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reason": reason,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = CardsAttachResponse500Type0Status(d.pop("status"))

        reason = CardsAttachResponse500Type0Reason(d.pop("reason"))

        message = d.pop("message")

        cards_attach_response_500_type_0 = cls(
            status=status,
            reason=reason,
            message=message,
        )

        cards_attach_response_500_type_0.additional_properties = d
        return cards_attach_response_500_type_0

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
