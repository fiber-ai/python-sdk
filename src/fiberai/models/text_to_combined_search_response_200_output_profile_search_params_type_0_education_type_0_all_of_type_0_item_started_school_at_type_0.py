from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0_strategy import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0_range_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0,
    )


T = TypeVar(
    "T",
    bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0",
)


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0:
    """
    Attributes:
        strategy (TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchool
            AtType0Strategy):
        range_ (None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedS
            choolAtType0RangeType0 | Unset):
    """

    strategy: TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0Strategy
    range_: (
        None
        | TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0_range_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0,
        )

        strategy = self.strategy.value

        range_: dict[str, Any] | None | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        elif isinstance(
            self.range_,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0,
        ):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0_range_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0,
        )

        d = dict(src_dict)
        strategy = TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0Strategy(
            d.pop("strategy")
        )

        def _parse_range_(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0.from_dict(
                    data
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AllOfType0ItemStartedSchoolAtType0RangeType0
                | Unset,
                data,
            )

        range_ = _parse_range_(d.pop("range", UNSET))

        text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0 = cls(
            strategy=strategy,
            range_=range_,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_education_type_0_all_of_type_0_item_started_school_at_type_0

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
