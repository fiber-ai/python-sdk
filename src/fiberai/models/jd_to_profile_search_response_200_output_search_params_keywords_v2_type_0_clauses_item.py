from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jd_to_profile_search_response_200_output_search_params_keywords_v2_type_0_clauses_item_operator import (
    JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator,
)

T = TypeVar("T", bound="JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItem")


@_attrs_define
class JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItem:
    """
    Attributes:
        operator (JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator):  Default:
            JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator.OR.
        terms (list[str]):
        negate (bool):  Default: False.
    """

    terms: list[str]
    operator: JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator = (
        JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator.OR
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
        operator = JdToProfileSearchResponse200OutputSearchParamsKeywordsV2Type0ClausesItemOperator(d.pop("operator"))

        terms = cast(list[str], d.pop("terms"))

        negate = d.pop("negate")

        jd_to_profile_search_response_200_output_search_params_keywords_v2_type_0_clauses_item = cls(
            operator=operator,
            terms=terms,
            negate=negate,
        )

        jd_to_profile_search_response_200_output_search_params_keywords_v2_type_0_clauses_item.additional_properties = d
        return jd_to_profile_search_response_200_output_search_params_keywords_v2_type_0_clauses_item

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
