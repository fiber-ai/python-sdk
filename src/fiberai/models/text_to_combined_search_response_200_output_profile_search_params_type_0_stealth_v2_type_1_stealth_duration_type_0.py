from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_period import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Period,
)

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_range import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range,
    )


T = TypeVar(
    "T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0"
)


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0:
    """
    Attributes:
        range_ (TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range):
        period (TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Period):
    """

    range_: TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range
    period: TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_.to_dict()

        period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range": range_,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_range import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range,
        )

        d = dict(src_dict)
        range_ = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range.from_dict(
            d.pop("range")
        )

        period = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Period(
            d.pop("period")
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0 = cls(
            range_=range_,
            period=period,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0

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
