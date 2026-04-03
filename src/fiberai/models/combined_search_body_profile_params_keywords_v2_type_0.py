from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_body_profile_params_keywords_v2_type_0_operator import (
    CombinedSearchBodyProfileParamsKeywordsV2Type0Operator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_body_profile_params_keywords_v2_type_0_clauses_item import (
        CombinedSearchBodyProfileParamsKeywordsV2Type0ClausesItem,
    )
    from ..models.combined_search_body_profile_params_keywords_v2_type_0_options_type_0 import (
        CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0,
    )


T = TypeVar("T", bound="CombinedSearchBodyProfileParamsKeywordsV2Type0")


@_attrs_define
class CombinedSearchBodyProfileParamsKeywordsV2Type0:
    """
    Attributes:
        clauses (list[CombinedSearchBodyProfileParamsKeywordsV2Type0ClausesItem]):
        operator (CombinedSearchBodyProfileParamsKeywordsV2Type0Operator | Unset):  Default:
            CombinedSearchBodyProfileParamsKeywordsV2Type0Operator.AND.
        options (CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0 | None | Unset):
    """

    clauses: list[CombinedSearchBodyProfileParamsKeywordsV2Type0ClausesItem]
    operator: CombinedSearchBodyProfileParamsKeywordsV2Type0Operator | Unset = (
        CombinedSearchBodyProfileParamsKeywordsV2Type0Operator.AND
    )
    options: CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_profile_params_keywords_v2_type_0_options_type_0 import (
            CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0,
        )

        clauses = []
        for clauses_item_data in self.clauses:
            clauses_item = clauses_item_data.to_dict()
            clauses.append(clauses_item)

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clauses": clauses,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_profile_params_keywords_v2_type_0_clauses_item import (
            CombinedSearchBodyProfileParamsKeywordsV2Type0ClausesItem,
        )
        from ..models.combined_search_body_profile_params_keywords_v2_type_0_options_type_0 import (
            CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0,
        )

        d = dict(src_dict)
        clauses = []
        _clauses = d.pop("clauses")
        for clauses_item_data in _clauses:
            clauses_item = CombinedSearchBodyProfileParamsKeywordsV2Type0ClausesItem.from_dict(clauses_item_data)

            clauses.append(clauses_item)

        _operator = d.pop("operator", UNSET)
        operator: CombinedSearchBodyProfileParamsKeywordsV2Type0Operator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CombinedSearchBodyProfileParamsKeywordsV2Type0Operator(_operator)

        def _parse_options(data: object) -> CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CombinedSearchBodyProfileParamsKeywordsV2Type0OptionsType0 | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        combined_search_body_profile_params_keywords_v2_type_0 = cls(
            clauses=clauses,
            operator=operator,
            options=options,
        )

        combined_search_body_profile_params_keywords_v2_type_0.additional_properties = d
        return combined_search_body_profile_params_keywords_v2_type_0

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
