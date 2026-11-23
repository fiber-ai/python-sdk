from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item_reason import (
    ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItemReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem")


@_attrs_define
class ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem:
    """
    Attributes:
        identifier (str): The LinkedIn vanity slug of the person (extracted from the URL if you provided one), as stored
            when they were added to the list.
        reason (ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItemReason): Why this identifier
            failed to resolve. 'profile_not_found' means no profile exists for it — a deleted account or a malformed
            identifier.
        last_checked_at (datetime.datetime | None | Unset): When this identifier was last checked for resolution. Null
            if it was never checked.
    """

    identifier: str
    reason: ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItemReason
    last_checked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        reason = self.reason.value

        last_checked_at: None | str | Unset
        if isinstance(self.last_checked_at, Unset):
            last_checked_at = UNSET
        elif isinstance(self.last_checked_at, datetime.datetime):
            last_checked_at = self.last_checked_at.isoformat()
        else:
            last_checked_at = self.last_checked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "reason": reason,
            }
        )
        if last_checked_at is not UNSET:
            field_dict["lastCheckedAt"] = last_checked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        reason = ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItemReason(d.pop("reason"))

        def _parse_last_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_checked_at = _parse_last_checked_at(d.pop("lastCheckedAt", UNSET))

        list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item = cls(
            identifier=identifier,
            reason=reason,
            last_checked_at=last_checked_at,
        )

        list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item.additional_properties = d
        return list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item

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
