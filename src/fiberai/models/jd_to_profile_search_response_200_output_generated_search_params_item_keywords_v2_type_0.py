from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_operator import (
    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_clauses_item import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0ClausesItem,
    )
    from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_options_type_0 import (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0,
    )


T = TypeVar("T", bound="JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0")


@_attrs_define
class JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0:
    """
    Attributes:
        operator (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator):  Default:
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator.AND.
        clauses (list[JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0ClausesItem]):
        options (JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0 | None | Unset):
    """

    clauses: list[JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0ClausesItem]
    operator: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator = (
        JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator.AND
    )
    options: JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_options_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0,
        )

        operator = self.operator.value

        clauses = []
        for clauses_item_data in self.clauses:
            clauses_item = clauses_item_data.to_dict()
            clauses.append(clauses_item)

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(
            self.options, JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0
        ):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "clauses": clauses,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_clauses_item import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0ClausesItem,
        )
        from ..models.jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0_options_type_0 import (
            JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0,
        )

        d = dict(src_dict)
        operator = JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0Operator(d.pop("operator"))

        clauses = []
        _clauses = d.pop("clauses")
        for clauses_item_data in _clauses:
            clauses_item = (
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0ClausesItem.from_dict(
                    clauses_item_data
                )
            )

            clauses.append(clauses_item)

        def _parse_options(
            data: object,
        ) -> JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = (
                    JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0.from_dict(
                        data
                    )
                )

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JdToProfileSearchResponse200OutputGeneratedSearchParamsItemKeywordsV2Type0OptionsType0 | None | Unset,
                data,
            )

        options = _parse_options(d.pop("options", UNSET))

        jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0 = cls(
            operator=operator,
            clauses=clauses,
            options=options,
        )

        jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0.additional_properties = d
        return jd_to_profile_search_response_200_output_generated_search_params_item_keywords_v2_type_0

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
