from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reverse_phone_lookup_response_200_output_rejection_reason_type_0 import (
        ReversePhoneLookupResponse200OutputRejectionReasonType0,
    )
    from ..models.reverse_phone_lookup_response_200_output_results_item_type_0 import (
        ReversePhoneLookupResponse200OutputResultsItemType0,
    )
    from ..models.reverse_phone_lookup_response_200_output_results_item_type_1 import (
        ReversePhoneLookupResponse200OutputResultsItemType1,
    )


T = TypeVar("T", bound="ReversePhoneLookupResponse200Output")


@_attrs_define
class ReversePhoneLookupResponse200Output:
    """
    Attributes:
        results (list[ReversePhoneLookupResponse200OutputResultsItemType0 |
            ReversePhoneLookupResponse200OutputResultsItemType1]): LinkedIn profiles or companies matching this phone
            number. Usually contains one result.
        rejection_reason (None | ReversePhoneLookupResponse200OutputRejectionReasonType0 | Unset): Present when the
            phone number is unresolvable (e.g. invalid format, not found).
    """

    results: list[
        ReversePhoneLookupResponse200OutputResultsItemType0 | ReversePhoneLookupResponse200OutputResultsItemType1
    ]
    rejection_reason: None | ReversePhoneLookupResponse200OutputRejectionReasonType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reverse_phone_lookup_response_200_output_rejection_reason_type_0 import (
            ReversePhoneLookupResponse200OutputRejectionReasonType0,
        )
        from ..models.reverse_phone_lookup_response_200_output_results_item_type_0 import (
            ReversePhoneLookupResponse200OutputResultsItemType0,
        )

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, ReversePhoneLookupResponse200OutputResultsItemType0):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        rejection_reason: dict[str, Any] | None | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        elif isinstance(self.rejection_reason, ReversePhoneLookupResponse200OutputRejectionReasonType0):
            rejection_reason = self.rejection_reason.to_dict()
        else:
            rejection_reason = self.rejection_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reverse_phone_lookup_response_200_output_rejection_reason_type_0 import (
            ReversePhoneLookupResponse200OutputRejectionReasonType0,
        )
        from ..models.reverse_phone_lookup_response_200_output_results_item_type_0 import (
            ReversePhoneLookupResponse200OutputResultsItemType0,
        )
        from ..models.reverse_phone_lookup_response_200_output_results_item_type_1 import (
            ReversePhoneLookupResponse200OutputResultsItemType1,
        )

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> (
                ReversePhoneLookupResponse200OutputResultsItemType0
                | ReversePhoneLookupResponse200OutputResultsItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = ReversePhoneLookupResponse200OutputResultsItemType0.from_dict(data)

                    return results_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_1 = ReversePhoneLookupResponse200OutputResultsItemType1.from_dict(data)

                return results_item_type_1

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        def _parse_rejection_reason(
            data: object,
        ) -> None | ReversePhoneLookupResponse200OutputRejectionReasonType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rejection_reason_type_0 = ReversePhoneLookupResponse200OutputRejectionReasonType0.from_dict(data)

                return rejection_reason_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReversePhoneLookupResponse200OutputRejectionReasonType0 | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejectionReason", UNSET))

        reverse_phone_lookup_response_200_output = cls(
            results=results,
            rejection_reason=rejection_reason,
        )

        reverse_phone_lookup_response_200_output.additional_properties = d
        return reverse_phone_lookup_response_200_output

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
