from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_profile_params_keywords_v2_type_0_clauses_item_operator import (
    CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItem")


@_attrs_define
class CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItem:
    """
    Attributes:
        terms (list[str]):
        operator (CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator | Unset):  Default:
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator.OR.
        negate (bool | Unset):  Default: False.
    """

    terms: list[str]
    operator: CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator | Unset = (
        CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator.OR
    )
    negate: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms = self.terms

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        negate = self.negate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "terms": terms,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if negate is not UNSET:
            field_dict["negate"] = negate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        terms = cast(list[str], d.pop("terms"))

        _operator = d.pop("operator", UNSET)
        operator: CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CombinedSearchCountBodyProfileParamsKeywordsV2Type0ClausesItemOperator(_operator)

        negate = d.pop("negate", UNSET)

        combined_search_count_body_profile_params_keywords_v2_type_0_clauses_item = cls(
            terms=terms,
            operator=operator,
            negate=negate,
        )

        combined_search_count_body_profile_params_keywords_v2_type_0_clauses_item.additional_properties = d
        return combined_search_count_body_profile_params_keywords_v2_type_0_clauses_item

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
