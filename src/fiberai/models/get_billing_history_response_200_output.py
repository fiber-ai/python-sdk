from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_billing_history_response_200_output_entries_item_type_0 import (
        GetBillingHistoryResponse200OutputEntriesItemType0,
    )
    from ..models.get_billing_history_response_200_output_entries_item_type_1 import (
        GetBillingHistoryResponse200OutputEntriesItemType1,
    )


T = TypeVar("T", bound="GetBillingHistoryResponse200Output")


@_attrs_define
class GetBillingHistoryResponse200Output:
    """
    Attributes:
        entries (list[GetBillingHistoryResponse200OutputEntriesItemType0 |
            GetBillingHistoryResponse200OutputEntriesItemType1]): Purchase history, newest first.
    """

    entries: list[
        GetBillingHistoryResponse200OutputEntriesItemType0 | GetBillingHistoryResponse200OutputEntriesItemType1
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_billing_history_response_200_output_entries_item_type_0 import (
            GetBillingHistoryResponse200OutputEntriesItemType0,  # noqa: PLC0415
        )

        entries = []
        for entries_item_data in self.entries:
            entries_item: dict[str, Any]
            if isinstance(entries_item_data, GetBillingHistoryResponse200OutputEntriesItemType0):
                entries_item = entries_item_data.to_dict()
            else:
                entries_item = entries_item_data.to_dict()

            entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_billing_history_response_200_output_entries_item_type_0 import (
            GetBillingHistoryResponse200OutputEntriesItemType0,  # noqa: PLC0415
        )
        from ..models.get_billing_history_response_200_output_entries_item_type_1 import (
            GetBillingHistoryResponse200OutputEntriesItemType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:

            def _parse_entries_item(
                data: object,
            ) -> (
                GetBillingHistoryResponse200OutputEntriesItemType0 | GetBillingHistoryResponse200OutputEntriesItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_0 = GetBillingHistoryResponse200OutputEntriesItemType0.from_dict(data)

                    return entries_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entries_item_type_1 = GetBillingHistoryResponse200OutputEntriesItemType1.from_dict(data)

                return entries_item_type_1

            entries_item = _parse_entries_item(entries_item_data)

            entries.append(entries_item)

        get_billing_history_response_200_output = cls(
            entries=entries,
        )

        get_billing_history_response_200_output.additional_properties = d
        return get_billing_history_response_200_output

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
