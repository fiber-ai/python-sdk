from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0_suffix_type_1 import (
    TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1,
)
from ..models.text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0_suffix_type_2_type_1 import (
    TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1,
)
from ..models.text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0_suffix_type_3_type_1 import (
    TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1,
)

T = TypeVar("T", bound="TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0")


@_attrs_define
class TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0:
    """
    Attributes:
        quantity (float):
        suffix (None | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1 |
            TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1 |
            TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1):
    """

    quantity: float
    suffix: (
        None
        | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1
        | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1
        | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        suffix: None | str
        if isinstance(self.suffix, TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1):
            suffix = self.suffix.value
        elif isinstance(
            self.suffix, TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1
        ):
            suffix = self.suffix.value
        elif isinstance(
            self.suffix, TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1
        ):
            suffix = self.suffix.value
        else:
            suffix = self.suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "suffix": suffix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        def _parse_suffix(
            data: object,
        ) -> (
            None
            | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1
            | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1
            | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_1 = TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1(data)

                return suffix_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_2_type_1 = (
                    TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1(data)
                )

                return suffix_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_3_type_1 = (
                    TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1(data)
                )

                return suffix_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType1
                | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType2Type1
                | TextToCompanySearchResponse200OutputSearchParamsRevenueUSDType0MinType0SuffixType3Type1,
                data,
            )

        suffix = _parse_suffix(d.pop("suffix"))

        text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0 = cls(
            quantity=quantity,
            suffix=suffix,
        )

        text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0.additional_properties = d
        return text_to_company_search_response_200_output_search_params_revenue_usd_type_0_min_type_0

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
