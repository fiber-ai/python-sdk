from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cards_attach_response_409_reason import CardsAttachResponse409Reason
from ..models.cards_attach_response_409_status import CardsAttachResponse409Status

T = TypeVar("T", bound="CardsAttachResponse409")


@_attrs_define
class CardsAttachResponse409:
    """
    Attributes:
        status (CardsAttachResponse409Status):
        reason (CardsAttachResponse409Reason):
        message (str):
    """

    status: CardsAttachResponse409Status
    reason: CardsAttachResponse409Reason
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
        status = CardsAttachResponse409Status(d.pop("status"))

        reason = CardsAttachResponse409Reason(d.pop("reason"))

        message = d.pop("message")

        cards_attach_response_409 = cls(
            status=status,
            reason=reason,
            message=message,
        )

        cards_attach_response_409.additional_properties = d
        return cards_attach_response_409

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
