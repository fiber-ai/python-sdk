from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item import (
        ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem,
    )


T = TypeVar("T", bound="ListTrackerUnresolvedIdentifiersResponse200Output")


@_attrs_define
class ListTrackerUnresolvedIdentifiersResponse200Output:
    """
    Attributes:
        unresolved_identifiers (list[ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem]):
            Identifiers that could not be resolved to a profile and are NOT counted in personCount — most commonly because
            the profile does not exist (deleted account or malformed identifier). Use this to reconcile the identifiers you
            sent against personCount.
        total_unresolved_count (int): Total number of unresolved identifiers on this list, across all pages.
        pending_identifier_count (int): Number of identifiers still being resolved in the background. They count toward
            personCount until resolution finishes, at which point they either resolve or move to unresolvedIdentifiers.
        next_cursor (None | str): Cursor for fetching the next page. Null when there are no more results.
    """

    unresolved_identifiers: list[ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem]
    total_unresolved_count: int
    pending_identifier_count: int
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unresolved_identifiers = []
        for unresolved_identifiers_item_data in self.unresolved_identifiers:
            unresolved_identifiers_item = unresolved_identifiers_item_data.to_dict()
            unresolved_identifiers.append(unresolved_identifiers_item)

        total_unresolved_count = self.total_unresolved_count

        pending_identifier_count = self.pending_identifier_count

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unresolvedIdentifiers": unresolved_identifiers,
                "totalUnresolvedCount": total_unresolved_count,
                "pendingIdentifierCount": pending_identifier_count,
                "nextCursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_tracker_unresolved_identifiers_response_200_output_unresolved_identifiers_item import (
            ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        unresolved_identifiers = []
        _unresolved_identifiers = d.pop("unresolvedIdentifiers")
        for unresolved_identifiers_item_data in _unresolved_identifiers:
            unresolved_identifiers_item = (
                ListTrackerUnresolvedIdentifiersResponse200OutputUnresolvedIdentifiersItem.from_dict(
                    unresolved_identifiers_item_data
                )
            )

            unresolved_identifiers.append(unresolved_identifiers_item)

        total_unresolved_count = d.pop("totalUnresolvedCount")

        pending_identifier_count = d.pop("pendingIdentifierCount")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        list_tracker_unresolved_identifiers_response_200_output = cls(
            unresolved_identifiers=unresolved_identifiers,
            total_unresolved_count=total_unresolved_count,
            pending_identifier_count=pending_identifier_count,
            next_cursor=next_cursor,
        )

        list_tracker_unresolved_identifiers_response_200_output.additional_properties = d
        return list_tracker_unresolved_identifiers_response_200_output

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
