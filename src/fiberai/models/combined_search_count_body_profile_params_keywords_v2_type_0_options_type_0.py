from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0_field_selection_mode import (
    CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0_fields_to_search_over_type_0 import (
        CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0")


@_attrs_define
class CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0:
    """
    Attributes:
        field_selection_mode (CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode |
            Unset):  Default: CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode.DEFAULT.
        fields_to_search_over (CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0 |
            None | Unset):
    """

    field_selection_mode: CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode | Unset = (
        CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode.DEFAULT
    )
    fields_to_search_over: (
        CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0_fields_to_search_over_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0,  # noqa: PLC0415
        )

        field_selection_mode: str | Unset = UNSET
        if not isinstance(self.field_selection_mode, Unset):
            field_selection_mode = self.field_selection_mode.value

        fields_to_search_over: dict[str, Any] | None | Unset
        if isinstance(self.fields_to_search_over, Unset):
            fields_to_search_over = UNSET
        elif isinstance(
            self.fields_to_search_over,
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0,
        ):
            fields_to_search_over = self.fields_to_search_over.to_dict()
        else:
            fields_to_search_over = self.fields_to_search_over

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_selection_mode is not UNSET:
            field_dict["fieldSelectionMode"] = field_selection_mode
        if fields_to_search_over is not UNSET:
            field_dict["fieldsToSearchOver"] = fields_to_search_over

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0_fields_to_search_over_type_0 import (
            CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_selection_mode = d.pop("fieldSelectionMode", UNSET)
        field_selection_mode: CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode | Unset
        if isinstance(_field_selection_mode, Unset):
            field_selection_mode = UNSET
        else:
            field_selection_mode = CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldSelectionMode(
                _field_selection_mode
            )

        def _parse_fields_to_search_over(
            data: object,
        ) -> CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_to_search_over_type_0 = (
                    CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0.from_dict(
                        data
                    )
                )

                return fields_to_search_over_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsKeywordsV2Type0OptionsType0FieldsToSearchOverType0 | None | Unset,
                data,
            )

        fields_to_search_over = _parse_fields_to_search_over(d.pop("fieldsToSearchOver", UNSET))

        combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0 = cls(
            field_selection_mode=field_selection_mode,
            fields_to_search_over=fields_to_search_over,
        )

        combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0.additional_properties = d
        return combined_search_count_body_profile_params_keywords_v2_type_0_options_type_0

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
