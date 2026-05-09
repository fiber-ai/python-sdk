from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_operator import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem,
    )
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_options_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0")


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0:
    """
    Attributes:
        operator (TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator):  Default:
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator.AND.
        clauses (list[TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem]):
        options (None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0 |
            Unset):
    """

    clauses: list[TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem]
    operator: TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator = (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator.AND
    )
    options: None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0 | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_options_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0,
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
            self.options, TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0
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
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_clauses_item import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0_options_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0,
        )

        d = dict(src_dict)
        operator = TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0Operator(
            d.pop("operator")
        )

        clauses = []
        _clauses = d.pop("clauses")
        for clauses_item_data in _clauses:
            clauses_item = (
                TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0ClausesItem.from_dict(
                    clauses_item_data
                )
            )

            clauses.append(clauses_item)

        def _parse_options(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = (
                    TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0.from_dict(
                        data
                    )
                )

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordsV2Type0OptionsType0 | Unset,
                data,
            )

        options = _parse_options(d.pop("options", UNSET))

        text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0 = cls(
            operator=operator,
            clauses=clauses,
            options=options,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_keywords_v2_type_0

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
