from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item_operator import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator,
)

T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem")


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem:
    """
    Attributes:
        operator (TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator):
            Default: TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator.OR.
        terms (list[str]):
        negate (bool):  Default: False.
    """

    terms: list[str]
    operator: TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator = (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator.OR
    )
    negate: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        terms = self.terms

        negate = self.negate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "terms": terms,
                "negate": negate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operator = TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItemOperator(
            d.pop("operator")
        )

        terms = cast(list[str], d.pop("terms"))

        negate = d.pop("negate")

        text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item = cls(
            operator=operator,
            terms=terms,
            negate=negate,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item

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
