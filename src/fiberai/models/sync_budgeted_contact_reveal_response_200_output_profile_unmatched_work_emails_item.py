from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item_status import (
    SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemStatus,
)
from ..models.sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item_type import (
    SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemType,
)

T = TypeVar("T", bound="SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem")


@_attrs_define
class SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItem:
    """
    Attributes:
        email (str):
        type_ (SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemType): Whether this address is a
            work email or a personal email.
        status (SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemStatus): Deliverability of this
            address. Only `valid` has passed a deliverability check.
    """

    email: str
    type_: SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemType
    status: SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_ = self.type_.value

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "type": type_,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        type_ = SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemType(d.pop("type"))

        status = SyncBudgetedContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemStatus(d.pop("status"))

        sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item = cls(
            email=email,
            type_=type_,
            status=status,
        )

        sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item.additional_properties = d
        return sync_budgeted_contact_reveal_response_200_output_profile_unmatched_work_emails_item

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
