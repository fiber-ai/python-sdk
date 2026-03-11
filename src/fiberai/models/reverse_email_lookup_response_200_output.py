from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reverse_email_lookup_response_200_output_data_item import ReverseEmailLookupResponse200OutputDataItem
    from ..models.reverse_email_lookup_response_200_output_rejection_type_0 import (
        ReverseEmailLookupResponse200OutputRejectionType0,
    )


T = TypeVar("T", bound="ReverseEmailLookupResponse200Output")


@_attrs_define
class ReverseEmailLookupResponse200Output:
    """
    Attributes:
        data (list[ReverseEmailLookupResponse200OutputDataItem]): LinkedIn profiles matching this email, ordered by best
            match. Usually contains one result.
        rejection (None | ReverseEmailLookupResponse200OutputRejectionType0 | Unset): Present when the email is
            unresolvable (e.g. disposable, anonymous relay, or role-based address). The request succeeded but there is no
            person to find.
    """

    data: list[ReverseEmailLookupResponse200OutputDataItem]
    rejection: None | ReverseEmailLookupResponse200OutputRejectionType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reverse_email_lookup_response_200_output_rejection_type_0 import (
            ReverseEmailLookupResponse200OutputRejectionType0,
        )

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        rejection: dict[str, Any] | None | Unset
        if isinstance(self.rejection, Unset):
            rejection = UNSET
        elif isinstance(self.rejection, ReverseEmailLookupResponse200OutputRejectionType0):
            rejection = self.rejection.to_dict()
        else:
            rejection = self.rejection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if rejection is not UNSET:
            field_dict["rejection"] = rejection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reverse_email_lookup_response_200_output_data_item import (
            ReverseEmailLookupResponse200OutputDataItem,
        )
        from ..models.reverse_email_lookup_response_200_output_rejection_type_0 import (
            ReverseEmailLookupResponse200OutputRejectionType0,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ReverseEmailLookupResponse200OutputDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_rejection(data: object) -> None | ReverseEmailLookupResponse200OutputRejectionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rejection_type_0 = ReverseEmailLookupResponse200OutputRejectionType0.from_dict(data)

                return rejection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReverseEmailLookupResponse200OutputRejectionType0 | Unset, data)

        rejection = _parse_rejection(d.pop("rejection", UNSET))

        reverse_email_lookup_response_200_output = cls(
            data=data,
            rejection=rejection,
        )

        reverse_email_lookup_response_200_output.additional_properties = d
        return reverse_email_lookup_response_200_output

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
